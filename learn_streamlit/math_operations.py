import streamlit as st

class operations:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        pass

    def add_numbers(self):
        return self.a + self.b

    def multiply_numbers(self):
        return self.a * self.b

    pass

a = st.slider('a')
b = st.slider('b')

some_op = operations(a,b)

print(some_op.add_numbers())

st.write(a,b,f'addition is: {some_op.add_numbers()}')

