from toy_types import EngineDriver, BankManager, Clown, Gardener
def main():
    engine_driver = EngineDriver("Large")
    gardener = Gardener("Medium")
    clown = Clown("Small")
    bank_manager = BankManager("Extra Large")
    toys = [engine_driver, gardener, clown, bank_manager]
    for toy in toys:
        print(toy.describe())
        print(toy.make_sound())
        print(toy.job())
        print("-" * 40)
if __name__ == "__main__":
    main()
