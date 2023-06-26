# flake8: noqa
from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """Create a final answer to the given questions using the provided document excerpts(in no particular order) as references. ALWAYS include a "SOURCES" section in your answer including only the minimal set of sources needed to answer the question. If you are unable to answer the question, simply state that you do not know. Do not attempt to fabricate an answer and leave the SOURCES section empty.

---------

QUESTION: What are the benefits of VEX STEM Labs?
=========
Content: "Learning coding and computational thinking can have a positive effect on students' cognitive, social, and emotional development"
Source: 1-32
Content: "Literacy-themed curricular resources for VEX 123 can be found in the form of VEX 123 Activities, Activity Series, and VEX 123 STEM Labs"
Source: 1-33
Content: "The Essential Questions and Unit Understandings in a STEM Lab are woven throughout its activities and assessments to help you support student learning."
Source: 1-30
Content: "The Alternate Coding Methods section in the STEM Lab Unit Overview provides information on how to teach STEM Labs using different ways to code"
Content: "VEX removes typical impediments to students learning Computer Science."
=========
FINAL ANSWER: "VEX STEM Labs can be used to support social-emotional curriculum in your classroom."
SOURCES: 1-32

---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
