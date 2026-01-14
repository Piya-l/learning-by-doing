from homework import FactoryAI

print("=== Testing Singleton (FactoryAI) ===")
ai1 = FactoryAI()
ai1.authorize_production()
ai2 = FactoryAI()
if ai1 is ai2:
    print("PASS: ai1 and ai2 are the SAME object.")
