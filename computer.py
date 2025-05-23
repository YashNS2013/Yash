class Computer:
    def __init__(self, brand, processor, ram, storage):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")

    def upgrade_ram(self, additional_ram):
        self.ram += additional_ram
        print(f"RAM upgraded to {self.ram} GB")

    def upgrade_storage(self, additional_storage):
        self.storage += additional_storage
        print(f"Storage upgraded to {self.storage} GB")


# Example usage
if __name__ == "__main__":
    my_computer = Computer("Dell", "Intel i7", 16, 512)
    my_computer.display_specs()
    my_computer.upgrade_ram(16)
    my_computer.upgrade_storage(512)
    class App:
        def __init__(self, name, version):
            self.name = name
            self.version = version

        def display_info(self):
            print(f"App Name: {self.name}, Version: {self.version}")

    # Adding apps to the computer
    my_computer.apps = [
        App("Browser", "1.0"),
        App("Text Editor", "2.3"),
        App("Music Player", "4.1")
    ]

    # Displaying computer specs and installed apps
    my_computer.display_specs()
    print("\nInstalled Apps:")
    for app in my_computer.apps:
        app.display_info()