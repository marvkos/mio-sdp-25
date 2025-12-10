class LightsService:

    def __init__(self, repository):
        self.repository = repository
    
    def toggle_light(self, light_id):
        light = self.repository.get(light_id)
        light["is_on"] = not light["is_on"]
        
        # If turning off, set brightness to 0
        # If turning on and brightness is 0, set to default 50
        if not light["is_on"]:
            light["brightness"] = 0
        elif light["brightness"] == 0:
            light["brightness"] = 50
        
        self.repository.update(light_id, light)
        return light
