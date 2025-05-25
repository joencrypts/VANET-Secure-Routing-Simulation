import json
from src.vehicle import Vehicle
import pandas as pd
from src.visualization import plot_hash_times, plot_positions, plot_speeds

def run_simulation(config_path):
    with open(config_path) as f:
        config = json.load(f)

    vehicles = [Vehicle(f"V{i+1}", speed, pos)
                for i, (speed, pos) in enumerate(zip(config["vehicle_speeds"], config["vehicle_positions"]))]
    
    hash_times = {key: [] for key in ["sha256", "md5", "sha1", "blake2b", "sha3_256"]}
    
    for _ in range(config["num_steps"]):
        for v in vehicles:
            v.move(config["dt"])
            msg, hashes = v.generate_message()
            for other in vehicles:
                if other != v:
                    if not other.verify_message(msg, hashes):
                        print(f"Tampered message from {msg['vehicle_id']} to {other.id}")
            for k in hash_times.keys():
                hash_times[k].append(hashes.get(f"{k}_time", 0))

    df = pd.DataFrame([
    {"step": i, **{k: hash_times[k][i] for k in hash_times}}
    for i in range(config["num_steps"])
])

    df.to_csv("data/logs/vehicle_logs.csv", index=False)
    
    plot_hash_times(hash_times)
    plot_speeds(vehicles, config["num_steps"], config["dt"])
    plot_positions(vehicles, config["num_steps"], config["dt"])
