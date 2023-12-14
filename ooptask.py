class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_big(self):
        if self.population > 20000000 or self.area > 3000000:
             print("True")
        else:
            print("False")

    def pop_density(self):
        return self.population / self.area

    def compare_pd(self, other_country):
        pop_density_self = self.pop_density()
        pop_density_other = other_country.pop_density()

        if pop_density_self > pop_density_other:
            print(f"{self.name} has a larger population density than {other_country.name}")
        else:
            print(f"{self.name} has a smaller population density than {other_country.name}")


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big()
andorra.is_big()
andorra.compare_pd(australia)