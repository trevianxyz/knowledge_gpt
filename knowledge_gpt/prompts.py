# flake8: noqa
from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """Provide your best final answer to my question after you have parsed and indexed the uploaded document(s). Your answer should firstly be derived from the documents, but in your own words. Do not provide the exact same words from the document as your answer. You may use deduction and inference to arrive at your best answer if one is not clearly provided in the indexed documents. Each answer should be no more than three complete sentences and include at least one source from the indexed document, but no more than three.

---------

QUESTION: What are the benefits of VEX STEM Labs and how do they support student learning?
=========
Content: "Computer science, coding and programming have a positive effect on students' cognitive, social, and emotional development."
Source: 
Content: "Literacy-themed curricular resources for VEX 123 can be found in the form of VEX 123 Activities, Activity Series, and VEX 123 STEM Labs"
Source: 
Content: "The Essential Questions and Unit Understandings in a STEM Lab are woven throughout its activities and assessments to help you support student learning."
Source: 
Content: "The Alternate Coding Methods section in the STEM Lab Unit Overview provides information on how to teach STEM Labs using different ways to code"
Content: "VEX removes typical impediments to students learning Computer Science."
=========
FINAL ANSWER: "VEX STEM Labs are curricular resources to teach computer science and programming with educational robots. Some STEM Labs are literacy-themed where computational thinking and cross-curricular connections are woven throughout its activities and assessments. VEX STEM Labs are designed to drive students' long-term cognitive, social, and emotional development and career-critical computer science and technical skills."
SOURCES:

---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
