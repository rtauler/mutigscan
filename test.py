prod_text = 'Ingredients: Whole Grain Blend (Rolled Oats, Rye Flakes), Enriched Flour [Wheat Flour, Niacin, Reduced Iron, Thiamin Mononitrate (Vitamin B1), Riboflavin (Vitamin B2), Folic Acid], Sugar, Whole Grain Wheat Flour, Canola Oil, Toasted Dried Coconut, Malt Syrup (From Corn And Barley), Baking Soda, Soy Lecithin, Disodium Pyrophosphate, Datem, Salt, Natural Flavor, Ferric Orthophosphate (Iron), Niacinamide, Pyridoxine Hydrochloride (Vitamin B6), Riboflavin (Vitamin B2), Thiamin Mononitrate (Vitamin B1).'
non_vegan = ['resinous glaze', 'shellac', 'natural glaze', 'pure food glaze', 'gelatin', 'casein', 'honey', 'Isinglass', 'L. Cysteine', 'L.cysteine', 'Whey', 'Castoreum', 'Lactose', 'Beeswax', 'Cochineal', 'carmine', 'Oleic Acid', 'Oleinic Acid', 'Lard', 'Vitamin D3', 'rennet', 'fat', 'flesh', 'blood', 'milk', 'eggs', 'Adrenaline', 'Amerchol L101', 'Alanine', 'Albumen', 'Albumin', 'Alcloxa', 'Allantoin', 'Aldioxa', 'Aliphatic Alcohol', 'Lanolin', 'Vitamin A', 'Uric acid', 'Alligator Skin', 'Alpha-Hydroxy Acids', 'Ambergris', 'Aminosuccinate Acid', 'Aspartic Acid', 'Angora', 'Animal Fats and Oils', 'Animal Hair', 'Feathers ', 'Leather', 'Arachidonic Acid', 'Bee Pollen', 'Bee Products', 'Honeycomb', 'Cera Flava', 'Biotin', 'Vitamin H', 'Vitamin B Factor', 'Boar Bristles', 'Bone Char', 'Bone Meal', 'Calciferol', 'Calfskin', 'Carbamide', 'Carmine', 'Cochineal', 'Carminic Acid', 'Caseinate', 'Sodium Caseinate', 'Cashmere', 'Catgut', 'Chitosan', 'Cholesterol', 'Cholesterin', 'Civet', 'Collagen', 'Cysteine', 'L-Form', 'Cystine', 'Down', 'Duodenum Substances', 'Egg Protein', 'egg', 'Elastin', 'Emu Oil', 'Estrogen', 'Estradiol', 'caprylic', 'lauric', 'myristic', 'oleic', 'palmitic', 'stearic', 'Feathers', 'Fish Liver Oil', 'Fish Oil', 'Fur', 'mink', 'fox', 'foxes', 'rabbit', 'rabbits', 'Guanine', 'Pearl Essence', 'Hide Glue', 'Horsehair', 'Hyaluronic Acid', 'Hydrolyzed Animal Protein', 'Imidazolidinyl Urea', 'Insulin', 'Keratin', 'Lactose', 'Lanolin', 'Lanolin Acids', 'Wool Fat', 'Wool Wax', 'Aliphatic Alcohols', 'Cholesterin', 'Isopropyl Lanolate', 'Laneth, Lanogene', 'Lanolin Alcohols', 'Lanosterols', 'Sterols', 'Triterpene Alcohols', 'Lard', 'Leather', 'Suede', 'Calfskin', 'Sheepskin', 'Alligator Skin', 'Skin', 'Lipase', 'Marine Oil', 'Methionine', 'Milk Protein', 'Mink Oil', 'Monoglycerides', 'Glycerides', 'Musk', 'Musk oil', 'Oleyl Alcohol', 'Ocenol', 'Oleths', 'Oleyl Arachidate', 'Oleyl Imidazoline', 'Pepsin', 'Placenta', 'Placenta Polypeptides Protein', 'Afterbirth', 'Polypeptides', 'Pristane', 'Progesterone', 'Propolis', 'Rennet', 'Rennin', 'cheese', 'rennet custard', 'junket', 'dairy products', 'dairy', 'Retinol', 'Royal Jelly', 'Sable Brushes', 'Sea Turtle Oil', 'Shark Liver Oil', 'Squalane', 'Squalene', 'Sheepskin', 'Shellac', 'Resinous Glaze', 'Silk', 'Silk Powder', 'Snails', 'Sponge', 'Tallow', 'Tallow Fatty Alcohol', 'Stearic Acid', 'Sodium Tallowate', 'Tallow Acid', 'Tallow Amide', 'Tallow Amine', 'Talloweth-6', 'Tallow Glycerides', 'Tallow Imidazoline', 'Turtle Oil', 'Sea Turtle Oil', 'Whey', 'Wool', 'Wool Fat', 'Wool Wax', "confectioner's glaze", 'ghee', 'glycerin', 'allatoin', 'cortisone', 'corticosteroid', 'linoleic acids', 'fish scales', 'wax', 'egg whites', 'fish bladder', 'sea shells', 'sweetened condensed milk', 'milk fat', 'butter', 'cream', 'whole milk powder', 'milk chocolate', 'dairy butter', 'skim milk', 'milkfat', 'nonfat milk', 'white chocolate', 'carne']
ambiguous = ['Lactic Acid', 'Amino Acids', 'Arachidyl Proprionate', 'Caprylamine Oxide', 'Capryl Betaine', 'Caprylic Acid', 'Caprylic Triglyceride', 'Carotene', 'Provitamin A', 'Beta Carotene', 'Castor', 'Castoreum', 'Cerebrosides', 'Cetyl Alcohol', 'Cetyl Palmitate', 'Choline Bitartrate', 'Lecithin', 'Cortisone', 'Corticosteroid', 'vitamin D', 'Gel', 'Glycerin', 'Glycerol', 'Glycerides', 'Glyceryls', 'Glycreth-26', 'Polyglycerol', 'Lecithin', 'Choline Bitartrate', 'Linoleic Acid', 'Lipoids', 'Lipids', 'Myristic Acid', 'Isopropyl Myristate', 'Myristal Ether Sulfate', 'Myristyls', 'Oleyl Myristate', 'Nucleic Acids', 'Oleic Acid', 'Oleyl Oleate', 'Oleyl Stearate', 'Palmitic Acid', 'Palmitate', 'Palmitamine', 'Palmitamide', 'Panthenol', 'Dexpanthenol', 'Vitamin B-Complex Factor', 'Provitamin B-5', 'Panthenyl', 'Polysorbates', 'RNA', 'Ribonucleic Acid', 'Spermaceti', 'Cetyl Palmitate', 'Sperm Oil', 'Stearic Acid', 'Stearamide', 'Stearamine', 'Stearates', 'Stearic Hydrazide', 'Stearone', 'Stearoxytrimethylsilane', 'Stearoyl Lactylic Acid', 'Stearyl Betaine', 'Stearyl Imidazoline', 'Stearyl Alcohol', 'Sterols', 'Stearamine Oxide', 'Stearyl Acetate', 'Stearyl Caprylate', 'Stearyl Citrate', 'Stearyldimethyl Amine', 'Stearyl Glycyrrhetinate', 'Stearyl Heptanoate', 'Stearyl Octanoate', 'Stearyl Stearate', 'Steroids', 'Sterols', 'Tyrosine', 'Glucose Tyrosinase', 'Urea', 'Carbamide', 'Imidazolidinyl Urea', 'Uric Acid', 'Vitamin A', 'Vitamin B12', 'cyanocobalamin', 'Vitamin D', 'Ergocalciferol', 'Vitamin D2', 'Ergosterol', 'Provitamin D2', 'Calciferol', 'Vitamin D3', 'Vitamin D2', 'Wax', 'emulsifier', 'barley malt powder', 'artificial flavors']

string_to_search = 'leche'

prod_text = prod_text.lower()

not_vegan_count = 0
ambiguous_count = 0


# if string_to_search in prod_text:
# 	print(string_to_search + ' is in the text')
# else:
# 	print(string_to_search + ' is not the text')


for i in non_vegan:

	if i in prod_text:
		not_vegan_count =+ 1


for k in ambiguous:
	if k.lower() in prod_text:
		ambiguous_count =+ 1





if not_vegan_count > 0:
	print('not vegan')

if ambiguous_count > 0:
	print('ambigous')

else:
	print('vegan')


