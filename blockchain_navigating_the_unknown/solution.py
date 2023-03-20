from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://165.232.98.11:31072"))

# interact with the contract
contract = w3.eth.contract(address="0x8c3d9b9c1b8b2b9f", abi=abi)

# put version=10 in the target contract 
