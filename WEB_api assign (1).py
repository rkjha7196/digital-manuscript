#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Q1. What is an API? Give an example, where an API is used in real life.
Q2. Give advantages and disadvantages of using API.
Q3. What is a Web API? Differentiate between API and Web API.
Q4. Explain REST and SOAP Architecture. Mention shortcomings of SOAP.
Q5. Differentiate between REST and SOAP.'''


# In[2]:


#1
'''API stands for Application Programming Interface. It is a set of rules and
protocols that allows different software applications to communicate and interact with each other.
In real life we uses APIs while transferring money from paytm wallet or Google pay to someone
else account'''

#2
'''Advantages:
1. APIs allow different software systems to integrate and communicate with each other seamlessly.
2. APIs promote modularity and code reusability. 
3. They allow developers to retrieve specific information or perform specific operations
without needing to understand the underlying implementation details.
 
   Disadvantages:
1. When using an API, your software becomes dependent on the stability
   and availability of the API provider
2. Working with APIs can be complex, especially when dealing with multiple
   APIs or integrating with complex systems.
3. APIs can expose sensitive data and functionality, making security and privacy
   considerations crucial. If an API is not properly secured, it can be vulnerable
   to attacks or unauthorized access.'''

#3
''' A Web API is an API specifically designed to be accessed over the web using HTTP
protocols. It enables communication between different software applications or 
services through the internet.

API: An API (Application Programming Interface) is a broader term that refers to a 
     set of rules and protocols that allow different software components to 
     interact and communicate with each other.
Web API: A Web API is a type of API that is accessed over the web using HTTP protocols.
         It typically follows the principles of Representational State Transfer (REST)architecture and 
         is designed to enable communication between different web-based systems or services.'''
#4
'''REST (Representational State Transfer):
   REST is an architectural style that provides guidelines for building web services.
   It is based on a set of principles and constraints that promote scalability, simplicity,
   and interoperability. RESTful services use HTTP as the communication protocol and rely on
   standard HTTP methods (GET, POST, PUT, DELETE) for performing operations on resources.
   
   SOAP (Simple Object Access Protocol):
   SOAP is a protocol that defines a set of rules for structuring messages and exchanging data
   between web services. SOAP allows communication between systems over different protocols, 
   such as HTTP, SMTP, or TCP. It uses XML for message format and provides a well-defined 
   contract through Web Services Description Language (WSDL).
   
   Shortcoming of SOAP:
   Non flexible, Complex, Non-cachable'''

#5
'''REST is commonly used for simpler, lightweight, and more scalable web services, while SOAP
is often used in enterprise-level applications that require robustness, security,
and complex data structures.'''



# In[ ]:




