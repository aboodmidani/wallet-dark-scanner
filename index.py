import streamlit as st
import requests

def check_address_reputation(address, blockchain):
    api_url = f"https://api.blockchain-reputation.com/check?address={address}&blockchain={blockchain}"
    try:
        response = requests.get(api_url, timeout=10)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            return {"error": "Failed to retrieve data. Try again later."}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Streamlit UI
st.title("Blockchain Address Reputation Checker")
st.write("Enter a blockchain address to check its reputation.")

# Input fields
address = st.text_input("Enter the blockchain address:")
blockchain = st.selectbox("Select Blockchain Type:", ["Bitcoin", "Ethereum", "Litecoin", "Dogecoin"])

if st.button("Check Reputation"):
    if address:
        result = check_address_reputation(address, blockchain.lower())
        st.subheader("Results:")
        if "error" in result:
            st.error(result["error"])
        else:
            st.json(result)
    else:
        st.warning("Please enter a valid blockchain address.")
