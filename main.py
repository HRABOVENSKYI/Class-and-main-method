class ElectricShaver:
    object_counter = 0

    def __init__(self, time_of_automatic_work_in_seconds=300, manufacturer="Xiaomi", number_of_razor_attachments=5,
                 price_in_hryvnias=200, warranty_time_in_years=1, body_material="Plastic"):
        self.time_of_automatic_work_in_seconds = time_of_automatic_work_in_seconds
        self.manufacturer = manufacturer
        self.number_of_razor_attachments = number_of_razor_attachments
        self.price_in_hryvnias = price_in_hryvnias
        self.warranty_time_in_years = warranty_time_in_years
        self.body_material = body_material
        ElectricShaver.object_counter += 1

    def __del__(self):
        ElectricShaver.object_counter -= 1

    def __str__(self):
        return f"ElectricShaver\nTime of automatic work in seconds: {self.time_of_automatic_work_in_seconds}\n" \
               f"Manufacturer: {self.manufacturer}\nNumber of razor attachments: {self.number_of_razor_attachments}\n" \
               f"Price in hryvnias: {self.price_in_hryvnias}\nWarranty time in years: {self.warranty_time_in_years}\n" \
               f"Body material: {self.body_material}\n"

    @staticmethod
    def get_object_counter():
        return ElectricShaver.object_counter


def main():
    electricShavers = [ElectricShaver(500, "Philips", 10, 2700, 1, "Aluminium and plastic"),
                       ElectricShaver(250, "Saturn"), ElectricShaver()]

    for electricShaver in electricShavers:
        print(electricShaver)

    print("Number of created objects of class ElectricShaver:", ElectricShaver.get_object_counter())


if __name__ == "__main__":
    main()
