from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

# Create a transaction
transaction = {
    'to': '0x1234567890123456789012345678901234567890',
    'value': 1000000000000000000,
    'gas': 21000,
    'gasPrice': 1000000000000000,
    'nonce': 0,
}

# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key='0x1234567890123456789012345678901234567890')

# Send the transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
