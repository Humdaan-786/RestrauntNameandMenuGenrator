from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

from keys import cohere_key

# Set up the Cohere LLM with your API key
llm = Cohere(cohere_api_key=cohere_key)

def gen_op(cusine):
    # Define the first prompt for generating the restaurant name
    restaurant_name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="Generate a single, unique, and catchy name for an Italian restaurant. Only return the name without explanations or multiple options."
    )

    # Define the chain for generating the restaurant name
    restaurant_name_chain = LLMChain(
        llm=llm,
        prompt=restaurant_name_prompt,
        output_key="restaurant_name"  # Output key for this chain
    )

# Define the second prompt for generating the menu
    menu_prompt = PromptTemplate(
        input_variables=["cuisine", "restaurant_name"],  # Use outputs from the first chain
        template=(
        "Create a short menu for a {cuisine} restaurant named {restaurant_name}. Include 2 appetizers, "
        "2 main courses, and 1 desserts with brief descriptions. Only return the menu."
    )
    )

# Define the chain for generating the menu
    menu_chain = LLMChain(
     llm=llm,
        prompt=menu_prompt,
        output_key="menu"  # Output key for this chain
    )

# Combine both chains into a sequential chain
    sequential_chain = SequentialChain(
        chains=[restaurant_name_chain, menu_chain],
        input_variables=["cuisine"],  # Initial input variable
        output_variables=["restaurant_name", "menu"]  # Final output variables
    )
    cuisine_type=cusine
    #   Use .apply() to handle multiple outputs
    output = sequential_chain.apply([{"cuisine": cuisine_type}])
    return output
  

# if __name__ == __name__:
#     print(gen_op("Italian"))