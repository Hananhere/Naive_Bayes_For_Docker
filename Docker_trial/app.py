import streamlit as st
import joblib
import time
from PIL import Image

def predict_gender(data):
    try:
        # Load the vectorizer and the trained model
        gender_nv_model = open("Model/Naive_Bayes_Model_For_Docker.pkl", "rb")
        gender_clf = joblib.load(gender_nv_model)
        cv = joblib.load("model/count_vectorizer.pkl")

        # Transform the input data using the loaded vectorizer
        vect = cv.transform(data).toarray()

        # Make predictions
        result = gender_clf.predict(vect)
        return result
    except Exception as e:
        print("An error occurred while loading the pickled files:", e)
        return None



def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)

def load_images(file_name):
  img = Image.open(file_name)
  return st.image(img,width=300)

def main():
  """Gender Classifier App
    With Streamlit

  """

  st.title("Gender Classifier")
  html_temp = """
  <div style="background-color:blue;padding:10px">
  <h2 style="color:grey;text-align:center;">Streamlit App </h2>
  </div>

  """
  st.markdown(html_temp,unsafe_allow_html=True)
  load_css('icon.css')
  

  name = st.text_input("Enter Name","Please Type Here")
  if st.button("Predict"):
    result = predict_gender([name])
    if result[0] == 0:
      prediction = 'Female'
      img = 'female.png'
    else:
      prediction = 'Male'
      img = 'male.png'

    st.success('Name: {} was classified as {}'.format(name.title(), prediction))
    load_images(img)

if __name__ == "__main__":
    main()
