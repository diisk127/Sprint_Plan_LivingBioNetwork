import random

class Route:
    def __init__(self, route_id, efficiency):
        self.id = route_id
        self.efficiency = efficiency
        self.maintenance_cost = 0.05

class NetworkState:
    def __init__(self):
        self.routes = [Route("Path_Alpha", 0.95), Route("Path_Beta", 0.40)]
        self.energy_pool = 1.0

    def get_best_route(self):
        # เลือกเส้นทางที่มีประสิทธิภาพ (efficiency) สูงสุดในขณะนั้น
        if not self.routes: return None
        return max(self.routes, key=lambda x: x.efficiency)

    def consume_energy(self):
        cost = sum(r.maintenance_cost for r in self.routes)
        self.energy_pool -= cost
        print(f"[Engine] Energy Reservoir: {self.energy_pool:.2f}")

    def spawn_new_path(self):
        if self.energy_pool >= 0.3:
            self.energy_pool -= 0.3
            new_id = f"Mycelium_{random.randint(100, 999)}"
            new_eff = random.uniform(0.6, 1.0)
            print(f"[Engine] Action: Spawning {new_id} (Efficiency: {new_eff:.2f})")
            self.routes.append(Route(new_id, new_eff))

def evolve_network(network_state):
    network_state.consume_energy()
    for route in list(network_state.routes):
        if route.efficiency < 0.5 or network_state.energy_pool < 0:
            print(f"[Engine] Action: Pruning {route.id} (Low efficiency/Energy)")
            network_state.routes.remove(route)
