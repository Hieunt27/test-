# import streamlit as st

# import os
# import pickle
# import sklearn

# spx = st.slider('SPX', min_value = 676.0, max_value = 2873.0, step = 0.1)

# # st.write('SPX: %f'%spx)

# st.slider('USO', min_value = 7.0, max_value = 118.0, step = 0.1)
# st.slider('SLV', min_value = 8.0, max_value = 48.0, step = 0.1)
# st.slider('EUR/USD', min_value = 1.0, max_value = 2.0, step = 0.1)
import streamlit as st
import os
import pickle


FILEPATH = os.path.join(os.getcwd(), 'demo_model', 'open.model.pkl')


def forecast(spx: float, uso: float, slv: float, eur_usd: float) -> float:
    model = pickle.load(open(FILEPATH, 'rb'))
    results = model.predict([[spx, uso, slv, eur_usd]])
    return results[0]


spx = st.slider('SPX', min_value=676.0, max_value=2873.0, step=0.1)
uso = st.slider('USO', min_value=8.0, max_value=118.0, step=0.1)
slv = st.slider('SLV', min_value=9.0, max_value=48.0, step=0.1)

eur_usd = st.slider('EUR/USD', min_value=1.0, max_value=2.0, step=0.1)

result = forecast(spx, uso, slv, eur_usd)
st.write('Predicted GLD: %s' % result)
