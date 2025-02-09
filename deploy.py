from mira_sdk import Flow, Client

client = Client(api_key="sb-eda68699859d11efcf2904add4a421c0")
flow1 = Flow(source="./my_flow.yaml")
deployment = client.flow.deploy(flow1)

print(f"Deployment ID: {deployment.id}")
print(f"Status: {deployment.status}")
print(f"API Endpoint: {deployment.endpoint}")