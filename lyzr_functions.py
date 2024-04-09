import base64
import requests
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.tasks.task_literals import InputType, OutputType

# Function to encode the image
def encode_image(image_path):
   with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')
  
# GPT VISION API
def explain_image(image_path, OPENAI_API_KEY):
    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    payload = {
      "model": "gpt-4-vision-preview",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "List all the input fields and their types in the image. Do not miss any detail. Return only the field name, type, options and is required or not. Avoid extra lines and extra details"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
              }
            }
          ]
        }
      ],
      "max_tokens": 700
    }

    image_response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    image_output = image_response.json()

    # output = {'id': 'chatcmpl-99nZoVi4OzxkBGvTcveaXeALIR6yi', 'object': 'chat.completion', 'created': 1712122552, 'model': 'gpt-4-1106-vision-preview', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': 'The image shows a subscription form with multiple input fields categorized into different sections. Here are the input fields and their types:\n\n1. Email address:\n   - Type: Text field, required (as indicated by the red asterisk *)\n\n2. First name:\n   - Type: Text field, required (as indicated by the red asterisk *)\n\n3. Last name:\n   - Type: Text field, required (as indicated by the red asterisk *)\n\nChoose Newsletters Section (Checkboxes to select newsletters):\n4. BizDaily - Top stories across all industries\n   - Type: Checkbox, option for "Daily”\n\n5. Africa\n   - Type: Checkbox, options for "Daily" and "Weekly”\n\n6. Marketing & Media\n   - Type: Checkbox, options for "Daily" and "Weekly”\n\n7. Retail\n   - Type: Checkbox, options for "Daily" and "Weekly”\n\n8. Agriculture\n   - Type: Checkbox, option for "Weekly”\n\n9. Automotive\n   - Type: Checkbox, option for "Weekly”\n\n10. Construction & Engineering\n    - Type: Checkbox, option for "Weekly”\n\n11. Education\n    - Type: Checkbox, option for "Weekly”\n\n12. Energy & Mining\n    - Type: Checkbox, option for "Weekly”\n\n13. Entrepreneurship\n    - Type: Checkbox, option for "Weekly”\n\n14. ESG & Sustainability\n    - Type: Checkbox, option for "Weekly”\n\n15. Finance\n    - Type: Checkbox, option for "Weekly”\n\n16. Healthcare\n    - Type: Checkbox, option for "Weekly”\n\n17. HR & Management\n    - Type: Checkbox, option for "Weekly”\n\n18. ICT\n    - Type: Checkbox, option for "Weekly”\n\n19. Legal\n    - Type: Checkbox, option for "Weekly”\n\n20. Lifestyle\n    - Type: Checkbox, option for "Weekly”\n\n21. Logistics & Transport\n    - Type: Checkbox, option for "Weekly”\n\n22. Manufacturing\n    - Type: Checkbox, option for "Weekly”\n\n23. Property\n    - Type: Checkbox, option for "Weekly”\n\n24. Tourism & Travel\n    - Type: Checkbox, option for "Weekly”\n\nAdditional Options Section (Checkboxes for additional email updates):\n25. Monthly stats\n    - Type: Checkbox, for opting to "Receive monthly email with stats from your account”\n\n26. Special offers\n    - Type: Checkbox, for opting to "Receive special offer emails from third parties and marketing communication from Bizcommunity, not more than four per month.”\n\nPlease note that the text fields for email address, first name, and last name are explicitly marked as required. The checkboxes allow the user to subscribe to various newsletters, with some having options for different frequencies like "Daily" or "Weekly." The last two checkboxes towards the bottom of the form are for subscribing to additional specific types of emails.'}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 790, 'completion_tokens': 590, 'total_tokens': 1380}, 'system_fingerprint': None}
    # output2 = {'id': 'chatcmpl-99nhBXqwPWzAHxPtVM9a0RdRV0VT3', 'object': 'chat.completion', 'created': 1712123009, 'model': 'gpt-4-1106-vision-preview', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': 'Field Name: Email address, Type: Text, Required: Yes\nField Name: First name, Type: Text, Required: Yes\nField Name: Last name, Type: Text, Required: Yes\n\nChoose Newsletters Section:\n- Field Name: BizDaily - Top stories across all industries, Type: Checkbox, Options: Daily, Required: No\n- Field Name: Africa, Type: Checkbox, Options: Daily, Weekly, Required: No\n- Field Name: Marketing & Media, Type: Checkbox, Options: Daily, Weekly, Required: No\n- Field Name: Retail, Type: Checkbox, Options: Daily, Weekly, Required: No\n- Field Name: Agriculture, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Automotive, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Construction & Engineering, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Education, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Energy & Mining, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Entrepreneurship, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: ESG & Sustainability, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Finance, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Healthcare, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: HR & Management, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: ICT, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Legal, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Lifestyle, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Logistics & Transport, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Manufacturing, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Property, Type: Checkbox, Options: Weekly, Required: No\n- Field Name: Tourism & Travel, Type: Checkbox, Options: Weekly, Required: No\n\nOther options:\n- Field Name: Monthly stats, Type: Checkbox, Required: No\n- Field Name: Special offers, Type: Checkbox, Required: No'}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 811, 'completion_tokens': 486, 'total_tokens': 1297}, 'system_fingerprint': None}

    image_result = image_output['choices'][0]['message']['content']
    
    return image_result

# CHAT MODEL
def generate_sample_inputs(image_result, OPENAI_API_KEY):
	# GPT 4 Text Model
	open_ai_model_text = OpenAIModel(
		api_key= OPENAI_API_KEY,
		parameters={
			"model": "gpt-4-turbo-preview",
			"temperature": 0.2,
			"max_tokens": 1500,
		},
	)

	field_generator = Agent(
		prompt_persona="You are an intelligent agent that can generate sample inputs for the fields provided",
		role="Input Generator",
	)

	field_generator_task = Task(
		name="HTML Input Generator",
		agent=field_generator,
		output_type=OutputType.TEXT,
		input_type=InputType.TEXT,
		model=open_ai_model_text,
		instructions="Generate sample inputs for the fields described in the input. Don't miss any input field.",
		log_output=False,
		enhance_prompt=False,
		default_input=image_result,
	).execute()

	# field_generator_task_output = ['Given the detailed description of the subscription form, here are sample inputs for each of the fields:\n\n1. **Email address:**\n   - Input: jane.doe@example.com\n\n2. **First name:**\n   - Input: Jane\n\n3. **Last name:**\n   - Input: Doe\n\n**Choose Newsletters Section:**\n\n4. **BizDaily - Top stories across all industries**\n   - Checked: Daily\n\n5. **Africa**\n   - Checked: Daily\n   - Checked: Weekly\n\n6. **Marketing & Media**\n   - Checked: Daily\n\n7. **Retail**\n   - Checked: Weekly\n\n8. **Agriculture**\n   - Checked: Weekly\n\n9. **Automotive**\n   - Checked: Weekly\n\n10. **Construction & Engineering**\n    - Checked: Weekly\n\n11. **Education**\n    - Checked: Weekly\n\n12. **Energy & Mining**\n    - Checked: Weekly\n\n13. **Entrepreneurship**\n    - Checked: Weekly\n\n14. **ESG & Sustainability**\n    - Checked: Weekly\n\n15. **Finance**\n    - Checked: Weekly\n\n16. **Healthcare**\n    - Checked: Weekly\n\n17. **HR & Management**\n    - Checked: Weekly\n\n18. **ICT**\n    - Checked: Weekly\n\n19. **Legal**\n    - Checked: Weekly\n\n20. **Lifestyle**\n    - Checked: Weekly\n\n21. **Logistics & Transport**\n    - Checked: Weekly\n\n22. **Manufacturing**\n    - Checked: Weekly\n\n23. **Property**\n    - Checked: Weekly\n\n24. **Tourism & Travel**\n    - Checked: Weekly\n\n**Additional Options Section:**\n\n25. **Monthly stats**\n    - Checked: Receive monthly email with stats from your account\n\n26. **Special offers**\n    - Checked: Receive special offer emails from third parties and marketing communication from Bizcommunity, not more than four per month']

	generated_fields_output = ''.join(field_generator_task)
	return generated_fields_output