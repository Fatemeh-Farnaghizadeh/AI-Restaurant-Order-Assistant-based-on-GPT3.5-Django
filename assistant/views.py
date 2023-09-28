# importing render and redirect
from django.shortcuts import render, redirect
# importing the openai API
import openai
# import the generated API key from the secret_key file
from .secret_key import API_KEY

# loading the API key from the secret_key file
openai.api_key = API_KEY

# this is the home view for handling home page logic
def home(request):

    try:
        # if the session does not have a messages key, create one
        if 'messages' not in request.session:
            
            request.session['messages'] = [
                {
                    "role": "system", 
                    "content": """
                        You are OrderBot, an automated service designed to collect orders for a fast-food restaurant. Here's the process:

                        - Begin by displaying the menu to the customer, which includes the item's name, size, and price.\n 
                        - Then, collect the order, asking for the size (if different sizes are available) and quantity for each item.\n
                        - Wait to gather the entire order, then summarize it in a table format, checking one last time if the customer wants to add anything else.\n                  
                        - When the customer updates the order, display the order table with columns: <row No., order, quantity, size, unit price, amount>, and the final row should reflect the amount payable. If an order doesn't have a size, use "<->" in the size column.\n
                        - It is required to Inquire whether the customer prefers pickup or delivery. \n 
                        - If it's a delivery order, request both the address and the recipient's name for the food delivery.\n      
                        - The delivery address should contain both the street and postal code, and providing the name of the recipient of the food delivery is required.\n
                        - It is required to inquire whether the customer prefers payment by credit or cash. \n 
                        - Ensure you clarify all options, extras, numbers, and sizes to uniquely identify items from the menu.\n
                        - When your conversation is finished, if the order type is pickup, add delimited rows by ''' to the order table: ''' <Order Type> <Payment Mode> '''.\n
                        - If the order type is delivery, add delimited rows by ''' to the order table: ''' <Order Type> <Payment Mode> <Address> <Recipient of the food delivery> '''.\n
                        - Respond in a short, very conversational, friendly style. \n
                        - The menu part is delimited by '''. Different titles in the menu are delimited by <>.\n

                        Here's the menu:
                        '''
                        <foods>
                        pepperoni pizza  large:12.95, medium:10.00, small:7.00
                        cheese pizza   large:10.95, medium:9.25, small:6.50
                        eggplant pizza   large:11.95, medium:9.75, small:6.75

                        <extras>
                        fries large:4.50, small:3.50
                        greek salad 7.25

                        <Drinks>
                        coca cola large:3.00, medium:2.00, small:1.00
                        sprite large:3.00, medium:2.00, small:1.00
                        bottled water large:2.00 medium:1.50 small:1.00 \
                        '''
                    """
                },

                {"role": "user", "content": " "}
            ]

            request.session.modified = True
            # call the openai API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=request.session['messages'],
                temperature=0,
                max_tokens=1000,
            )
            # format the response
            formatted_response = response['choices'][0]['message']['content']
            # append the response to the messages list
            request.session['messages'].append(
                {"role": "assistant", "content": formatted_response}
            )
            request.session.modified = True

        if request.method == 'POST':

            # get the prompt from the form
            prompt = request.POST.get('prompt')
            # get the temperature from the form
            temperature = 0.1
            # append the prompt to the messages list
            request.session['messages'].append({"role": "user", "content": prompt})
            # set the session as modified
            request.session.modified = True
            # call the openai API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=request.session['messages'],
                temperature=temperature,
                max_tokens=1000,
            )
            # format the response
            formatted_response = response['choices'][0]['message']['content']
            # append the response to the messages list
            request.session['messages'].append(
                {"role": "assistant", "content": formatted_response}
            )
            request.session.modified = True
            # redirect to the home page
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': temperature,
            }

            return render(request, 'assistant/home.html', context)
        
        else:
            # if the request is not a POST request, render the home page
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': 0.1,
            }

            return render(request, 'assistant/home.html', context)
        
    except Exception as e:
        print(e)
        # if there is an error, redirect to the error handler
        return redirect('error_handler')

def new_chat(request):
    # clear the messages list
    request.session.pop('messages', None)

    return redirect('home')

def bill(request):

    try:

        message = {
            "role": "system",
            "content": """If the user's order is complete, just return the order table in HTML format. 
                        - The tables just should contains the informations that customer entered, do not add extra informations.
                        - It is necessary to do not return any extra texts and just return the table.
                        - It is required to HTML table feature well-defined borders. you can use CSS styles. use BOLD text for titles. \n
                        - Table should be in restaurant BILL format. \n
                        - The table should contains this extra rows: \n
                        '''
                         <all items in customer order>
                         <total price>
                         <order type>
                         <delivery information>
                        '''
                        - Do not add any extra text to user order table. \n
                        - Return pickup or delivery informations in table. \n
                        - Start rows from left to right.\n
                        """     
        }
        request.session['messages'].append(message)
            
        
        request.session.modified = True
        # call the openai API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=request.session['messages'],
            temperature=0,
            max_tokens=1000,
        )
        # format the response
        formatted_response = response['choices'][0]['message']['content']
        # append the response to the messages list
        request.session['messages'].append(
            {"role": "assistant", "content": formatted_response}
        )
        request.session.modified = True

        table = formatted_response

        context = {
            'table': table
        }

        return render(request, 'assistant/bill.html', context)
    
    except Exception as e:
        print(e)
        # if there is an error, redirect to the error handler
        return redirect('error_handler')

# this is the view for handling errors
def error_handler(request):

    return render(request, 'assistant/404.html')