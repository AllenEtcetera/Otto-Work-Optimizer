import tkinter as tk
from tkinter import messagebox, ttk

# Function to reset window
def reset_window():
    global rootList
    rootList.destroy()
    create_window()

premade_lists_dict = {
    'Names': "Acre, Adair, Adrian, Alaska, Alex, Ali, Alva, Amani, Amari, An, Anchor, Arbor, Archie, Arden, Ari, Arie, Ariel, Aries, Arley, Armani, Armoni, Arrow, Artemis, Ash, Aspen, Aster, Aubrey, Auden, Austen, Avery, Ayomide, Azariah, Azriel, Azure, Bailey, Basil, Bay, Beacon, Bellamy, Bentley, Bergen, Berlin, Bex, Birch, Bird, Bix, Blair, Blake, Blue, Bo, Bowie, Branch, Breck, Brecken, Briar, Brighton, Britton, Brook, Bryce, Bryn, Cal, Callaway, Cam, Camdyn, Cameron, Campbell, Carey, Carlin, Carlisle, Carsyn, Casey, Cassidy, Cedar, Chandler, Charleston, Charlie, Clarke, Cleo, Clover, Coast, Cobalt, Colby, Collins, Comet, Cord, Courtney, Cove, Cree, Creek, Crimson, Crow, Cruise, Cruz, Cy, Cyan, Dakota, Dale, Dallas, Dana, Darcy, Dart, Dell, Demi, Denver, Derby, Devon, Dior, Drew, Duffy, Dune, Dusty, Easton, Echo, Egypt, Ellery, Ellington, Ellis, Ellison, Embry, Emerson, Ender, Enfys, Erie, Eris, Ever, Everest, Everette, Evren, Fable, Fallon, Fen, Fig, Finch, Finley, Fio, Francis, Frankie, Frey, Frost, Galaxy, Gale, Garland, Garnet, Gemini, Gentry, Gianni, Gift, Golden, Gray, Greer, Grey, Guadalupe, Hale, Halston, Harbor, Harlem, Harley, Harlow, Harp, Hart, Haven, Hayden, Henley, Holland, Hollis, Honor, Hopper, Hunter, Hutton, Iman, Indiana, Indigo, Indy, Ira, Isle, Jackie, Jael, Jagger, James, Jamie, Jan, Jay, Jaycee, Jaylin, Jazz, Jean, Jem, Jersey, Jesse, Jessie, Jett, Jody, Johnnie, Jory, Jove, Jude, Jules, July, Juniper, Jupiter, Justice, Kai, Kaidyn, Kapri, Karsyn, Kasey, Keaton, Keeley, Kelby, Kelly, Kelsey, Kendall, Kerry, Kester, Kestrel, Khari, Kiernan, Kim, Kimber, Kingsley, Kirby, Kit, Knight, Koda, Kodi, Koi, Kris, Lael, Laine, Lake, Laken, Lakota, Landry, Lane, Laramie, Lark, Larkin, Layne, Leaf, Lee, Lennon, Lennox, Leslie, Lex, Lexington, Linden, Lindsey, Link, Lock, London, Lou, Lowen, Loyal, Lucky, Lux, Luxury, Lynn, Lyric, Mackenzie, Majesty, Marion, Marley, Marlowe, Mars, Marvel, Mecca, Meridian, Merit, Merrill, Merritt, Micah, Michel, Milan, Miller, Mo, Moby, Morgan, Moss, Murphy, Natale, Nature, Navy, Nazareth, Night, Noel, Nova, Oakley, Ocean, October, Ollie, Onyx, Paget, Palmer, Pan, Paris, Park, Parker, Pat, Pax, Paz, Peace, Peak, Perry, Peyton, Phoenix, Pim, Pixel, Poe, Poet, Presley, Psalm, Puck, Quest, Quill, Quinby, Quincy, Quinn, Rain, Raleigh, Ramsey, Rana, Randy, Ray, Reagan, Reef, Reese, Reign, Remi, Remy, Rene, Revel, Reyes, Rhythm, Ricky, Ridley, Riley, Rio, Riot, Ripley, River, Robbie, Robin, Rogue, Rory, Rowan, Royal, Rumi, Rylen, Sage, Sailor, Salem, Sammie, Sandy, Santana, Sasha, Sawyer, Sayer, Sazz, Scout, Seneca, Seven, Shalom, Shannon, Shawn, Shea, Shelby, Sheridan, Shiloh, Sidney, Skyler, Sloan, Sol, Solo, Spark, Spencer, Stacy, Storm, Story, Sunny, Sutton, Tane, Tanner, Taran, Tarot, Tate, Tatum, Taylor, Teagan, Teal, Tempest, Temple, Terry, Tib, Tide, Tig, Tommie, Tracy, Troian, True, Truth, Tundra, Uduak, Urban, Vale, Valentine, Veer, Vesper, Viper, Waverly, West, Winter, Wisdom, Wren, Wylie, Wynn, Xenith, Yael, Yuri, Zaire, Zealand, Zen, Zenith, Zephyr, Zion, Zohar, Zuri",
    'Animals': "Aardvark, African Elephant, African Grey Parrot, African Lion, African Wild Dog, Agouti, Albacore, Albatross, Alligator, Alligator Gar, Allosaurus, Alpaca, Amazon Dolphin, Amazon Parrot, Amberjack, American Alligator, American Bison, American Crow, American Kestrel, American Robin, Anaconda, Anchovy, Andean Condor, Angelfish, Anglerfish, Anhinga, Anole, Ant, Anteater, Antelope, Arabian Horse, Arapaima, Arctic Fox, Arctic Wolf, Argus, Armadillo, Arowana, Arthropod, Asian Elephant, Assassin Bug, Atlantic Salmon, Auk, Axis Deer, Axolotl, Aye Aye, Badger, Bald Eagle, Baldpate, Ball Python, Bandicoot, Bar Jack, Barn Owl, Barn Swallow, Barnacle, Barracuda, Barred Owl, Basking Shark, Bat, Beaver, Beluga Whale, Bengal Tiger, Betta, Bichir, Bighorn Sheep, Binturong, Bird of Paradise, Black Angus, Black Bear, Black Buck, Black Dolphin, Black Footed Ferret, Black Mamba, Black Molly, Black Racer, Black Rail, Black Rat, Black Rhino, Black Sole, Black Swan, Black Swift, Black Widow Spider, Blackbird, Blacktip Shark, Blobfish, Blue Bull (Nilgai), Blue Catfish, Blue Duck, Blue Footed Booby, Blue Jay, Blue Marlin, Blue Runner, Blue Shark, Blue Tongue Skink, Blue Whale, Bluebird, Bluefin Tuna, Boa Constrictor, Bobcat, Bobwhite Quail, Bonefish, Bongo, Bonito, Bonobo, Booby Bird, Bottlenose Dolphin, Bowfin, Box Turtle, Brant, Bream, Brook Trout, Brown Bear, Brown Jay, Brown Pelican, Brown Recluse, Brown Snake, Brown Trout, Budgie, Buffalo, Buffalo Fish, Bufflehead, Bull Shark, Bullfrog, Bullhead, Bullsnake, Bunting, Burmese Python, Burrowing Owl, Bush Dog, Bushmaster, Butter Fish, Cacique, Caiman, California Condor, California Quail, Camel Spider, Canada Goose, Canary, Cane Toad, Canvasback, Capuchin, Capybara, Caracal, Carp, Cassowary, Cat Shark, Cat Snake, Catbird, Catfish, Cave Bear, Chachalaca, Chameleon, Chamois, Channel Catfish, Cheetah, Chickadee, Chimpanzee, Chinchilla, Chipmunk, Chukar, Cichlid, Cinnamon Teal, Clouded Leopard, Clydesdale, Coati, Cobia, Cobra, Cockatiel, Cockatoo, Cod, Coelacanth, Coho Salmon, Coley, Conger, Cooper's Hawk, Coot, Coral Snake, Cormorant, Corn Snake, Cory Catfish, Cottonmouth, Cottontail, Cow, Coyote, Crake, Crane, Crested Gecko, Crocodile, Crocodile Skink, Crow, Cuckoo Bird, Curlew, Cuscus, Dace, Danio, Deer Mouse, Deer Tick, Desert Tortoise, Diamondback Rattlesnake, Dik Dik, Dilophosaurus, Dimetrodon, Dingo, Dipper, Discus, Dodo, Dog Salmon, Dog Tick, Dogfish, Dolphin, Donkey, Dory, Dove, Drill, Duck, Dugong, Dwarf Hamster, Eagle, Eagle Owl, Echidna, Eel, Eider, Eland, Elephant Seal, Elephant Shrew, Elk, Emperor Penguin, Emu, Ermine, Escolar, Fainting Goat, Falcon, Fallow Deer, Fennec Fox, Ferret, Finch, Fisher, Fishing Cat, Flamingo, Florida Pompano, Flounder, Flycatcher, Flying Dragon, Flying Fox, Flying Squirrel, Fossa, Fox Squirrel, Friesian, Frigate Bird, Frilled Lizard, Frilled Shark, Frog, Gaboon Viper, Gadwall, Gannet, Gar, Garden Spider, Garter Snake, Gaur, Gazelle, Gecko, Genet, Gerbil, Gharial, Ghost Bat, Giant Ground Sloth, Giant Salamander, Gibbon, Gila Monster, Giraffe, Glow Worm, Gnu, Goat, Goblin Shark, Goby, Golden Cat, Golden Eagle, Golden Pheasant, Goldeneye, Goldfinch, Goldfish, Goliath Birdeater, Goose, Gopher, Gopher Snake, Gorilla, Goshawk, Gourami, Grackle, Grass Snake, Gray Fox, Gray Owl, Grayling, Great Blue Heron, Great White Shark, Green Anaconda, Green Frog, Green Jack, Green Jay, Green Turtle, Greenland Shark, Ground Squirrel, Groundhog, Grouse, Guan, Guanaco, Guinea Pig, Guppy, Haddock, Hagfish, Hake, Halibut, Hammerhead Shark, Hamster, Harlequin Duck, Harpy Eagle, Harrier Hawk, Hawk, Hedgehog, Hellbender, Hercules Beetle, Hermit Crab, Heron, Herring, Hippopotamus, Hobo Spider, Honey Badger, Horny Toad, Horse, Horseshoe Crab, House Finch, House Martin, House Mouse, House Sparrow, House Wren, Howler Monkey, Hummingbird, Humpback Whale, Huntsman Spider, Hyena, Ibis, Iguana, Impala, Indian Elephant, Irish Elk, Island Fox, Jack Dempsey, Jack Fish, Jackal, Jackrabbit, Jaeger, Jaguar, Kaka, Kakapo, Kangaroo, Kangaroo Rat, Kea, Key Deer, Killdeer, Killer Bee, Killer Whale (Orca), King Cobra, King Eider, King Salmon, Kingfisher, Kinkajou, Kit Fox, Kite, Kiwi, Knifefish, Koala, Kob, Kodiak Bear, Koi, Komodo Dragon, Kookaburra, Kudu, Kune Kune, Ladybug, Lake Sturgeon, Lake Trout, Lake Whitefish, Lamprey, Leatherback Sea Turtle, Lemming, Lemon Shark, Lemur, Leopard, Leopard Cat, Leopard Gecko, Leopard Seal, Leopard Shark, Lionfish, Lizard, Llama, Loach, Loggerhead Turtle, Lone Star Tick, Loon, Loris, Lovebird, Lynx, Lyrebird, Macaque, Macaw, Mackerel, Magpie, Mako Shark, Mallard Duck, Mamba, Manatee, Mandarin Duck, Mandrill, Maned Wolf, Manta Ray, Map Turtle, Mara, Marlin, Marmoset, Marmot, Marten, Mastadon, Meadowlark, Megalodon, Merganser, Merino Sheep, Merlin, Milk Fish, Milk Snake, Mink, Minnow, Mite, Moa, Moccasin, Mockingbird, Mole, Mole Rat, Molly, Moloch, Mongoose, Monitor Lizard, Monkfish, Moon Bear, Moon Fish, Moose, Moray Eel, Mountain Beaver, Mountain Goat, Mountain Lion, Mountain Sheep, Mourning Dove, Mule, Mule Deer, Muscovy Duck, Musk Ox, Muskrat, Mustang, Naked Mole Rat, Narwhal, Nene, Neon Tetra, Newt, Night Heron, Nighthawk, Northern Cardinal, Northern Pike, Nuthatch, Nutria Rat, Oarfish, Ocelot, Oil Fish, Okapi, Opossum, Orangutan, Orb Weaver, Oriole, Oscar Fish, Osprey, Ostrich, Paca, Pack Rat, Pacman Frog, Paint Horse, Painted Turtle, Panda Bear, Pangolin, Panther Chameleon, Parrot, Parrotfish, Partridge, Peacock, Pelican, Percheron, Peregrine Falcon, Permit, Petrel, Pheasant, Pig, Pigeon, Pika, Pike, Pileated Woodpecker, Pink Salmon, Pintail, Piranha, Pit Viper, Pitta, Platy, Platypus, Pleco, Plover, Poison Dart Frog, Polar Bear, Pollock, Pomfret, Pompano, Porcupine, Porpoise, Possum, Pot Belly Pig, Prairie Chicken, Prairie Dog, Proboscis Monkey, Ptarmigan, Puffin, Purple Martin, Pygmy Goat, Python, Quagga, Quarter Horse, Quetzal, Quokka, Rabbit, Raccoon, Rail, Rainbow Snake, Rainbow Trout, Rat, Rat Snake, Rat Squirrel, Raven, Red Angus, Red Deer, Red Fox, Red Panda, Red Squirrel, Red Tailed Hawk, Red Wolf, Redwing, Reef Shark, Reindeer, Remora, Reticulated Python, Rhea, Rhinoceros, Ringtail, River Otter, Roadrunner, Rudd, Ruddy Duck, Ruff, Russian Tortoise, Saber Tooth Tiger, Sable, Sage Grouse, Saiga Antelope, Sailfish, Salamander, Salmon, Saltwater Crocodile, Sambar, Sand Boa, Sand Cat, Sanderling, Sandhill Crane, Sandpiper, Savannah Monitor, Sawfish, Scarlet Ibis, Scorpion, Screamer, Screech Owl, Sea Dragon, Sea Eagle, Sea Horse, Sea Lion, Sea Otter, Sea Snake, Sea Turtle, Serval, Shad, Shearwater, Sheep, Shoebill Stork, Shrew, Shrike, Siberian Tiger, Siren, Skate, Skimmer, Skink, Skipjack, Skunk, Sloth, Sloth Bear, Slow Loris, Smelt, Snake, Snakehead, Snapping Turtle, Snipe, Snow Goose, Snow Leopard, Snowy Owl, Sockeye Salmon, Softshell Turtle, Sole, Sora, Spanish Mackerel, Sperm Whale, Spider, Spider Monkey, Spinosaurus, Spoonbill, Sprat, Springbok, Squirrel, Squirrel Monkey, Starling, Stegosaurus, Stingray, Stork, Sturgeon, Sugar Glider, Sulcata Tortoise, Sun Bear, Sunbird, Sunfish, Swallow, Swan, Swift, Swordfish, Taipan, Takin, Tamarin, Tanager, Tanuki, Tapir, Tarantula, Tarpon, Tarsier, Tasmanian Devil, Tegu Lizard, Tench, Tern, Tetra, Thoroughbred, Thresher Shark, Thrush, Tick, Tiger, Tiger Beetle, Tiger Shark, Tiger Snake, Timber Rattlesnake, Titanoboa, Titmouse, Toad, Tokay Gecko, Tortoise, Toucan, Towhee, Tree Frog, Tree Kangaroo, Triceratops, Triggerfish, Trilobite, Trout, Trumpeter Swan, Tuco Tuco, Tuna, Tundra Swan, Tur, Turkey, Turkey Vulture, Turtle, Turtle Dove, Tyrannosaurus, Uromastyx, Vampire Bat, Vaquita, Veiled Chameleon, Velociraptor, Vicuna, Viper, Vireo, Vole, Vulture, Wahoo, Wallaby, Walrus, Wandering Albatross, Warthog, Water Buffalo, Water Deer, Water Dragon, Water Monitor, Waxwing, Weasel, Weaver, Whale Shark, White Hawk, White Marlin, White Rhino, Whitefish, Whitetail Deer, Whiting, Whooping Crane, Wild Boar, Wild Horse, Wild Turkey, Willet, Wolf Snake, Wolverine, Wombat, Wood Duck, Woodcock, Woodpecker, Yak, Yellowfin Tuna, Yellowtail, Zebra, Zebrafish, Zebu, Zonkey",
    'Countries': "Afghanistan, Albania, Algeria, Andorra, Angola, Antigua and Barbuda, Argentina, Armenia, Australia, Austria, Azerbaijan, The Bahamas, Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bhutan, Bolivia, Bosnia and Herzegovina, Botswana, Brazil, Brunei, Bulgaria, Burkina Faso, Burundi, Cabo Verde, Cambodia, Cameroon, Canada, Central African Republic, Chad, Chile, China, Colombia, Comoros, Democratic Republic of the Congo, Republic of the Congo, Costa Rica, Côte d'Ivoire, Croatia, Cuba, Cyprus, Czech Republic, Denmark, Djibouti, Dominica, Dominican Republic, East Timor, Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia, Eswatini, Ethiopia, Fiji, Finland, France, Gabon, The Gambia, Georgia, Germany, Ghana, Greece, Grenada, Guatemala, Guinea, Guinea-Bissau, Guyana, Haiti, Honduras, Hungary, Iceland, India, Indonesia, Iran, Iraq, Ireland, Israel, Italy, Jamaica, Japan, Jordan, Kazakhstan, Kenya, Kiribati, North Korea, South Korea, Kosovo, Kuwait, Kyrgyzstan, Laos, Latvia, Lebanon, Lesotho, Liberia, Libya, Liechtenstein, Lithuania, Luxembourg, Madagascar, Malawi, Malaysia, Maldives, Mali, Malta, Marshall Islands, Mauritania, Mauritius, Mexico, Federated States of Micronesia, Moldova, Monaco, Mongolia, Montenegro, Morocco, Mozambique, Myanmar, Namibia, Nauru, Nepal, Netherlands, New Zealand, Nicaragua, Niger, Nigeria, North Macedonia, Norway, Oman, Pakistan, Palau, Panama, Papua New Guinea, Paraguay, Peru, Philippines, Poland, Portugal, Qatar, Romania, Russia, Rwanda, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Samoa, San Marino, Sao Tome and Principe, Saudi Arabia, Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Slovakia, Slovenia, Solomon Islands, Somalia, South Africa, Spain, Sri Lanka, Sudan, South Sudan, Suriname, Sweden, Switzerland, Syria, Taiwan, Tajikistan, Tanzania, Thailand, Togo, Tonga, Trinidad and Tobago, Tunisia, Turkey, Turkmenistan, Tuvalu, Uganda, Ukraine, United Arab Emirates, United Kingdom, United States, Uruguay, Uzbekistan, Vanuatu, Vatican City, Venezuela, Vietnam, Yemen, Zambia, Zimbabwe",
    'Numbers Ascending': ', '.join([str(i) for i in range(1, 1001)]),
    'Numbers Descending': ', '.join([str(i) for i in range(1000, 0, -1)]),
    'Letters Ascending': 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z',
    'Letters Descending': 'Z, Y, X, W, V, U, T, S, R, Q, P, O, N, M, L, K, J, I, H, G, F, E, D, C, B, A',
    'Alphanumeric Ascending': 'A1, B2, C3, 1A, 2B, 3C, 4D, 5E, 6F, 7G, 8H, 9I, 10J, 11K, 12L, 13N, 14M, 15O, 16P, 17Q, 18R, 19S, 20T, 21U, 22V, 23W, 24X, 25Y, 26Z',
    'Alphanumeric Descending': '26Z, 25Y, 24X, 23W, 22V, 21U, 20T, 19S, 18R, 17Q, 16P, 15O, 14N, 13M, 12L, 11K, 10J, 9I, 8H, 7G, 6F, 5E, 4D, 3C, 2B, 1A, C3, B2, A1'
}

# Get list, separator, and format from user
def get_list_and_separator():
    items = items_entry.get()
    num_items = num_items_entry.get()
    separator = separator_entry.get() or ' '  # Default to space
    list_format = list_combo.get()
    premade_key = items_combo.get()
    # Form text into list
    if premade_key in premade_lists_dict:
        try:
            num_items = int(num_items)
        except ValueError:
            num_items = premade_lists_dict[premade_key].count(',') + 1

        items_list = premade_lists_dict[premade_key].split(', ')[:num_items]
    else:
        items_list = items.split(separator)
    formatted_list = ''
    if list_format and items_list:
        if list_format == 'Standard English':
            formatted_list = ', '.join(items_list[:-1]) + ' and ' + items_list[-1] + '.'
        elif list_format == 'Python List':
            formatted_list = '[' + ', '.join(items_list) + ']'
        elif list_format == 'Python Tuple':
            formatted_list = '(' + ', '.join(items_list) + ')'
        elif list_format == 'C# List':
            formatted_list = 'new List<string> {' + ', '.join(items_list) + '}'
        elif list_format == 'C# Tuple':
            formatted_list = 'new Tuple<' + ', '.join(items_list) + '>()'
        elif list_format == 'Erlang List':
            formatted_list = '[' + ', '.join(items_list) + ']'
        elif list_format == 'Erlang Tuple':
            formatted_list = '{' + ', '.join(items_list) + '}'
        elif list_format == 'Powershell List':
            formatted_list = '@(' + ', '.join(items_list) + ')'
        elif list_format == 'Powershell Tuple':
            formatted_list = ',$(' + ', '.join(items_list) + ')'
        elif list_format == 'HTML List':
            formatted_list = '<ul>\n' + '\n'.join([f'  <li>{item}</li>' for item in items_list]) + '\n</ul>'
        elif list_format == 'CSS List':
            formatted_list = 'content: "' + ', '.join(items_list) + '";'
        elif list_format == 'JSON Array':
            formatted_list = '[' + ', '.join(f'"{item}"' for item in items_list) + ']'
        else:
            messagebox.showerror("Error", "Invalid list format selected")
        def copy_to_clipboard():
                formatted_list_window.clipboard_clear() # Clear clipboard
                formatted_list_window.clipboard_append(formatted_list) # Append new text to clipboard
                formatted_list_window.destroy()
                messagebox.showinfo("Clipboard", "List copied to clipboard!")

        # Show formatted list
        formatted_list_window = tk.Toplevel(rootList)
        formatted_list_window.title("Formatted List")
        formatted_list_label = tk.Label(formatted_list_window, text=formatted_list, wraplength=400)
        formatted_list_label.pack(pady=10)
        copy_button = tk.Button(formatted_list_window, text="Copy to Clipboard", command=copy_to_clipboard)
        copy_button.pack(pady=10)
    else:
        messagebox.showerror("Error", "All fields must be provided")

# Create window
def create_window():
    global rootList, items_entry, separator_entry, list_combo, items_combo, premade_lists, num_items_entry
    rootList = tk.Tk()
    rootList.title("Otto List")

    # Items entry
    items_label = tk.Label(rootList, text="Enter text:")
    items_label.pack(pady=5)
    items_entry = tk.Entry(rootList, width=50)
    items_entry.pack(pady=5)

    # Separator entry
    separator_label = tk.Label(rootList, text="Enter the separator character:")
    separator_label.pack()
    separator_entry = tk.Entry(rootList, width=5)
    separator_entry.pack(pady=5)

    # Premade lists
    premade_lists = list(premade_lists_dict.keys())
    items_label = tk.Label(rootList, text="Select premade list:")
    items_label.pack()
    items_combo = ttk.Combobox(rootList, values=premade_lists, width=50)
    items_combo.pack(pady=5)

    # Number of items entry
    num_items_label = tk.Label(rootList, text="Enter number of items:")
    num_items_label.pack(pady=5)
    num_items_entry = tk.Entry(rootList, width=5)
    num_items_entry.pack(pady=5)

    # List conversion type
    list_types = ['Standard English', 'Python List', 'Python Tuple', 'C# List', 'C# Tuple',
                  'Erlang List', 'Erlang Tuple', 'Powershell List', 'Powershell Tuple',
                  'HTML List', 'CSS List', 'JSON Array']
    list_label = tk.Label(rootList, text="Select list format:")
    list_label.pack(pady=5)
    list_combo = ttk.Combobox(rootList, values=list_types, width=50)
    list_combo.pack(pady=5)

    # Get List button
    get_list_button = tk.Button(rootList, text="Get List", command=get_list_and_separator)
    get_list_button.pack(pady=5)

    # Reset button
    reset_button = tk.Button(rootList, text="Reset", command=reset_window)
    reset_button.pack(pady=5)

    # Main loop
    rootList.mainloop()

create_window()