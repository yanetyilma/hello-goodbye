class delivery_personnel:
#Constructor
	def __init__(self, name, years_of_service, company, is_drone, zip_codes_covered):
		self.name				= name
		self.years_of_service	= years_of_service
		self.company 			= company
		self.is_drone			= is_drone
		self.zip_codes_covered	= zip_codes_covered
#Getters
	def get_years_of_service(self):
		return(self.years_of_service)
	def get_company(self):
		return(self.company)
	def get_zip_codes_covered(self):
		return(self.zip_codes_covered)
#Setters
	def set_years_of_service(self, d):
		self.years_of_service = d
	def set_company(self, d):
		self.company = d
	def set_zip_codes_covered(self, d):
		self.zip_codes_covered = d

def fact(codes):
	if(zip_codes_covered == 1):
		return(1)
	else:
		return(zip_codes_covered*fact(zip_codes_covered-1))

def main():
	zip_codes_covered = [2921,2019,2736,2617]

	for x in zip_codes_covered:
		if x == zip_codes_covered:
			print(x)

if __name__ == '__main__':
	main()