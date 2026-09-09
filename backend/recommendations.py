# Centralized disease recommendations and care guidance for all 38 PlantVillage classes

RECOMMENDATIONS = {
    # ---------------- Apple ----------------
    "Apple___Apple_scab": {
        "title": "Apple Scab (Venturia inaequalis)",
        "is_healthy": False,
        "description": "A serious fungal disease causing olive-green to black velvety spots on leaves and fruit, leading to premature leaf drop and deformed fruit.",
        "recommendations": [
            "Prune and dispose of infected leaves and twigs to reduce fungal spore load.",
            "Apply targeted fungicides (e.g., copper-based or sulfur sprays) during early spring bud break.",
            "Rake and destroy fallen leaves in autumn to disrupt the fungus overwintering cycle."
        ],
        "prevention": [
            "Plant scab-resistant apple cultivars (e.g., Liberty, Enterprise, Freedom).",
            "Maintain an open tree canopy through regular pruning to promote rapid leaf drying."
        ]
    },
    "Apple___Black_rot": {
        "title": "Apple Black Rot (Botryosphaeria obtusa)",
        "is_healthy": False,
        "description": "A fungal pathogen causing leaf frog-eye spots, cankers on branches, and firm brown-to-black rot on ripening fruit.",
        "recommendations": [
            "Prune out dead wood, mummified fruits, and cankered limbs during dormant season.",
            "Apply captan or sulfur-based protective fungicides from pink bud stage through harvest.",
            "Sanitize pruning shears with 70% alcohol between cuts to prevent spreading spores."
        ],
        "prevention": [
            "Remove all mummified fruit hanging on branches or lying on the ground.",
            "Avoid mechanical injuries to tree bark during harvesting and mowing."
        ]
    },
    "Apple___Cedar_apple_rust": {
        "title": "Cedar Apple Rust (Gymnosporangium juniperi-virginianae)",
        "is_healthy": False,
        "description": "A fungal rust requiring both apple trees and nearby Eastern red cedar/juniper hosts to complete its life cycle, producing bright yellow-orange leaf spots.",
        "recommendations": [
            "Apply appropriate protective fungicides (e.g., myclobutanil or mancozeb) in spring as leaves emerge.",
            "Inspect nearby cedar and juniper trees and remove gelatinous rust galls if feasible.",
            "Collect and dispose of heavily infected leaves before spores spread."
        ],
        "prevention": [
            "Avoid planting apple trees within 1 to 2 miles of juniper or red cedar trees.",
            "Select rust-resistant apple varieties such as Redfree, Enterprise, or Pristine."
        ]
    },
    "Apple___healthy": {
        "title": "Healthy Apple Foliage",
        "is_healthy": True,
        "description": "The apple leaf shows healthy green coloration with no visible signs of fungal or bacterial infection.",
        "recommendations": [
            "Maintain consistent drip irrigation, especially during dry spells and fruit development.",
            "Apply a balanced, slow-release fertilizer in early spring based on soil test results.",
            "Conduct routine leaf and bark scouting for early signs of pests such as aphids and mites."
        ],
        "prevention": [
            "Prune annually in late winter to ensure excellent sunlight penetration and air circulation.",
            "Keep the tree base mulched and clear of weeds to prevent rodent and pest infestation."
        ]
    },

    # ---------------- Blueberry ----------------
    "Blueberry___healthy": {
        "title": "Healthy Blueberry Foliage",
        "is_healthy": True,
        "description": "The blueberry foliage is robust and free from pathogenic symptoms.",
        "recommendations": [
            "Maintain acidic soil conditions (pH 4.5 to 5.5) using elemental sulfur or organic pine needle mulch.",
            "Provide consistent moisture (blueberries have shallow roots susceptible to drying).",
            "Apply ammonium sulfate or ericaceous fertilizer during early spring."
        ],
        "prevention": [
            "Apply a 3-inch layer of organic bark or sawdust mulch to retain soil moisture.",
            "Scout for blueberry maggot, spotted wing drosophila, and powdery mildew."
        ]
    },

    # ---------------- Cherry ----------------
    "Cherry_(including_sour)___Powdery_mildew": {
        "title": "Cherry Powdery Mildew (Podosphaera clandestina)",
        "is_healthy": False,
        "description": "A fungal disease causing white powdery patches on young leaves, curled leaf margins, and stunted shoot growth.",
        "recommendations": [
            "Apply potassium bicarbonate, neem oil, or horticultural oils at the first sign of mildew.",
            "Use registered fungicides during warm, humid weather when risk is highest.",
            "Prune overcrowded shoots to increase air movement and sunlight throughout the canopy."
        ],
        "prevention": [
            "Avoid overhead irrigation which creates high humidity around new foliage.",
            "Monitor new terminal growth weekly during late spring and early summer."
        ]
    },
    "Cherry_(including_sour)___healthy": {
        "title": "Healthy Cherry Foliage",
        "is_healthy": True,
        "description": "The cherry foliage exhibits healthy vigor with no signs of fungal mildew, bacterial canker, or pest damage.",
        "recommendations": [
            "Water deeply at the base during fruit set and dry summer periods.",
            "Apply balanced fruit tree fertilizer in spring before flower bud burst.",
            "Maintain clean orchard floor by clearing fallen leaves and dropped fruit."
        ],
        "prevention": [
            "Prune during dry summer periods to reduce the risk of bacterial canker infection.",
            "Apply organic mulch around the drip line to conserve soil moisture."
        ]
    },

    # ---------------- Corn (Maize) ----------------
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "title": "Corn Gray Leaf Spot (Cercospora zeae-maydis)",
        "is_healthy": False,
        "description": "A destructive fungal foliar disease producing rectangular, grayish-brown lesions bordered by leaf veins.",
        "recommendations": [
            "Apply foliar strobilurin or triazole fungicides at tasseling stage if disease pressure is high.",
            "Plow under or chop crop residues post-harvest to accelerate decomposition of fungal debris.",
            "Avoid continuous corn-on-corn planting to break pathogen buildup in soil."
        ],
        "prevention": [
            "Plant certified corn hybrids with high genetic resistance to Gray Leaf Spot.",
            "Implement a minimum 2-year crop rotation with non-host crops like soybeans."
        ]
    },
    "Corn_(maize)___Common_rust_": {
        "title": "Corn Common Rust (Puccinia sorghi)",
        "is_healthy": False,
        "description": "A fungal disease characterized by cinnamon-brown to dark brown powdery pustules on both upper and lower leaf surfaces.",
        "recommendations": [
            "Apply registered fungicides if rust pustules appear on upper leaves before tasseling.",
            "Monitor weather forecasts; rust develops rapidly during cool, humid conditions.",
            "Ensure balanced nitrogen nutrition; excess nitrogen can exacerbate rust severity."
        ],
        "prevention": [
            "Utilize corn hybrids with specific Rp resistance genes or high general rust tolerance.",
            "Plant early in the season to allow crops to mature before spore loads peak."
        ]
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "title": "Corn Northern Leaf Blight (Exserohilum turcicum)",
        "is_healthy": False,
        "description": "A fungal disease causing large, cigar-shaped, grayish-green to tan lesions on foliage that reduce grain fill.",
        "recommendations": [
            "Apply fungicide if lesions appear on the ear leaf or higher two weeks before or after silking.",
            "Chop and incorporate crop residue into the soil after harvest to reduce overwintering fungi.",
            "Rotate fields with non-grass crops such as legumes or brassicas."
        ],
        "prevention": [
            "Select hybrids featuring single-gene (Ht) or multi-gene resistance to Northern Leaf Blight.",
            "Practice minimum 1-year crop rotation out of corn."
        ]
    },
    "Corn_(maize)___healthy": {
        "title": "Healthy Corn Foliage",
        "is_healthy": True,
        "description": "The maize leaves are robust, deep green, and free from foliar blights, rusts, or nutrient deficiencies.",
        "recommendations": [
            "Provide adequate nitrogen, phosphorus, and potassium split-applied at key growth stages.",
            "Ensure sufficient irrigation during critical tasseling and silking windows.",
            "Keep fields weed-free during the first 6 weeks of growth to avoid nutrient competition."
        ],
        "prevention": [
            "Follow recommended seed spacing to maintain optimal plant population density.",
            "Scout regularly for corn rootworm, armyworms, and early leaf blight symptoms."
        ]
    },

    # ---------------- Grape ----------------
    "Grape___Black_rot": {
        "title": "Grape Black Rot (Guignardia bidwellii)",
        "is_healthy": False,
        "description": "A severe fungal disease causing reddish-brown leaf spots with black fruiting bodies and shriveled, black mummified berries.",
        "recommendations": [
            "Apply protective fungicides (e.g., captan, myclobutanil, or mancozeb) starting at early shoot growth.",
            "Prune out infected canes and remove all mummified grape clusters from the vines and ground.",
            "Maintain trellis canopy management to increase sunlight exposure and air circulation."
        ],
        "prevention": [
            "Ensure vine rows are oriented parallel to prevailing winds for rapid foliage drying.",
            "Select black-rot tolerant grape varieties where possible."
        ]
    },
    "Grape___Esca_(Black_Measles)": {
        "title": "Grape Esca / Black Measles (Phaeomoniella chlamydospora complex)",
        "is_healthy": False,
        "description": "A complex fungal trunk disease causing 'tiger-stripe' interveinal leaf discoloration, wood decay, and berry spotting.",
        "recommendations": [
            "Prune during dry weather in late winter to prevent fungal spores from entering fresh pruning cuts.",
            "Apply pruning wound sealants containing fungicides to major pruning cuts.",
            "Mark severely infected vines for surgical trunk renewal or vine replacement."
        ],
        "prevention": [
            "Minimize large pruning wounds on older wood.",
            "Avoid vine stress through balanced irrigation and balanced crop load management."
        ]
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "title": "Grape Leaf Blight (Pseudocercospora cladosporioides)",
        "is_healthy": False,
        "description": "A fungal infection causing irregular brown to dark lesions on leaves, leading to premature defoliation and poor fruit ripening.",
        "recommendations": [
            "Apply broad-spectrum copper or mancozeb sprays post-bloom if leaf spots are detected.",
            "Trim and tuck shoots into trellis wires to improve air movement through the vine canopy.",
            "Collect and destroy fallen infected leaves in late autumn."
        ],
        "prevention": [
            "Avoid overhead sprinkler irrigation that keeps grape leaves wet for prolonged periods.",
            "Maintain balanced nitrogen fertilization to avoid overly dense succulent foliage."
        ]
    },
    "Grape___healthy": {
        "title": "Healthy Grapevine Foliage",
        "is_healthy": True,
        "description": "The grapevine foliage shows vibrant green color, strong shoot growth, and no signs of mildew, rot, or trunk disease.",
        "recommendations": [
            "Continue regular canopy management (shoot positioning, suckering, and leaf pulling).",
            "Maintain drip irrigation tailored to the vineyard growth stage and fruit development.",
            "Conduct routine leaf-petiole nutrition testing to guide fertilizer application."
        ],
        "prevention": [
            "Prune vines annually during dormant season to balance vegetative growth and fruit yield.",
            "Monitor vineyard regularly for early powdery mildew or phylloxera symptoms."
        ]
    },

    # ---------------- Orange / Citrus ----------------
    "Orange___Haunglongbing_(Citrus_greening)": {
        "title": "Citrus Greening / Huanglongbing (Candidatus Liberibacter asiaticus)",
        "is_healthy": False,
        "description": "A devastating bacterial disease vectored by the Asian citrus psyllid, causing asymmetrical blotchy yellowing on leaves, twig dieback, and bitter misshapen fruit.",
        "recommendations": [
            "Inspect trees closely for Asian citrus psyllid insects and apply approved systemic insecticides.",
            "Apply foliar nutritional sprays containing zinc, manganese, and potassium to support tree vitality.",
            "Contact your local agricultural extension service for official reporting and containment guidance."
        ],
        "prevention": [
            "Plant only certified disease-free nursery stock from certified screened greenhouses.",
            "Establish biological or chemical control programs against the Asian citrus psyllid vector."
        ]
    },

    # ---------------- Peach ----------------
    "Peach___Bacterial_spot": {
        "title": "Peach Bacterial Spot (Xanthomonas arboricola pv. pruni)",
        "is_healthy": False,
        "description": "A bacterial pathogen causing angular purple-brown leaf lesions that drop out creating a 'shot-hole' appearance, along with fruit pitting.",
        "recommendations": [
            "Apply copper-based bactericides at dormant and bud swell stages before bloom.",
            "Apply oxytetracycline sprays during early cover sprays if bacterial pressure is severe.",
            "Avoid excess nitrogen fertilization which promotes susceptible tender new growth."
        ],
        "prevention": [
            "Plant bacterial spot-resistant peach cultivars (e.g., Redhaven, Reliance, Bellaire).",
            "Avoid overhead irrigation and maintain open tree canopies for fast drying."
        ]
    },
    "Peach___healthy": {
        "title": "Healthy Peach Foliage",
        "is_healthy": True,
        "description": "The peach foliage shows vigorous growth and smooth, lesion-free green leaves.",
        "recommendations": [
            "Maintain uniform soil moisture, especially during stone formation and fruit sizing.",
            "Apply balanced fertilizer in early spring and thin heavy fruit loads to prevent limb breakage.",
            "Monitor under-leaf surfaces for spider mites and peach tree borer at the trunk base."
        ],
        "prevention": [
            "Prune in open-center vase system to maximize sunlight and airflow throughout the canopy.",
            "Apply a dormant copper spray in autumn after leaf drop to protect against leaf curl."
        ]
    },

    # ---------------- Pepper (Bell) ----------------
    "Pepper,_bell___Bacterial_spot": {
        "title": "Bell Pepper Bacterial Spot (Xanthomonas campestris pv. vesicatoria)",
        "is_healthy": False,
        "description": "A bacterial infection causing small water-soaked leaf spots that turn brown with yellow halos, leading to severe defoliation and sunburned fruit.",
        "recommendations": [
            "Apply copper bactericide combined with mancozeb for improved efficacy.",
            "Remove and destroy severely infected lower leaves to limit upward splashing of bacteria.",
            "Avoid working in the pepper patch while foliage is wet from rain or dew."
        ],
        "prevention": [
            "Use certified disease-free, hot-water treated seeds or resistant pepper varieties.",
            "Use drip irrigation rather than overhead sprinklers to keep foliage dry."
        ]
    },
    "Pepper,_bell___healthy": {
        "title": "Healthy Bell Pepper Foliage",
        "is_healthy": True,
        "description": "The pepper foliage is healthy, vibrant green, and free from bacterial spots, viral mottling, or insect damage.",
        "recommendations": [
            "Provide 1 to 1.5 inches of water per week using drip irrigation.",
            "Apply a balanced calcium-rich fertilizer to prevent blossom end rot.",
            "Stake or cage pepper plants to support heavy fruit load and prevent branch breakage."
        ],
        "prevention": [
            "Mulch with straw or black plastic to regulate soil temperature and suppress weeds.",
            "Rotate nightshade crops on a 3-year cycle to prevent soil-borne pathogens."
        ]
    },

    # ---------------- Potato ----------------
    "Potato___Early_blight": {
        "title": "Potato Early Blight (Alternaria solani)",
        "is_healthy": False,
        "description": "A common fungal disease producing characteristic dark brown 'target-board' concentric ring spots on older leaves, progressing upwards.",
        "recommendations": [
            "Apply protective fungicides (e.g., chlorothalonil, mancozeb, or copper) when lower leaves show symptoms.",
            "Maintain optimal plant nutrition; plants stressed by low nitrogen are more susceptible.",
            "Avoid overhead irrigation in late afternoon or evening to minimize leaf wetness duration."
        ],
        "prevention": [
            "Practice a minimum 3-year crop rotation with non-solanaceous crops.",
            "Plant certified disease-free seed tubers and maintain proper plant spacing."
        ]
    },
    "Potato___Late_blight": {
        "title": "Potato Late Blight (Phytophthora infestans)",
        "is_healthy": False,
        "description": "A highly destructive water-mold pathogen causing large water-soaked dark lesions with white fungal growth on leaf undersides during cool, moist conditions.",
        "recommendations": [
            "Apply targeted systemic late blight fungicides immediately upon detection.",
            "Promptly destroy and bag infected vines; do not add infected tissue to compost piles.",
            "Hill up soil around potato stems to create a barrier protecting tubers from washing spores."
        ],
        "prevention": [
            "Plant certified late-blight resistant potato varieties (e.g., Kennebec, Defender, Elba).",
            "Monitor local late blight forecasting networks and eliminate volunteer potato plants."
        ]
    },
    "Potato___healthy": {
        "title": "Healthy Potato Foliage",
        "is_healthy": True,
        "description": "The potato foliage shows strong, healthy green growth with no signs of early or late blight.",
        "recommendations": [
            "Continue hilling soil around stems to encourage tuber development and prevent tuber greening.",
            "Maintain consistent soil moisture throughout tuber initiation and bulking stages.",
            "Scout regularly for Colorado potato beetles, aphids, and early foliar spots."
        ],
        "prevention": [
            "Practice crop rotation with legumes or grains.",
            "Allow potato vines to fully die down 2 weeks before harvest to set durable tuber skins."
        ]
    },

    # ---------------- Raspberry ----------------
    "Raspberry___healthy": {
        "title": "Healthy Raspberry Foliage",
        "is_healthy": True,
        "description": "The raspberry cane and leaf foliage is vigorous, healthy, and free from anthracnose or rust fungi.",
        "recommendations": [
            "Provide support trellises to keep canes upright and well-aerated.",
            "Water regularly at soil level; raspberries have shallow root systems.",
            "Apply balanced berry fertilizer or compost in early spring."
        ],
        "prevention": [
            "Prune out spent floricanes immediately after fruiting to improve airflow.",
            "Keep the base mulched with wood chips or straw to suppress weeds and conserve moisture."
        ]
    },

    # ---------------- Soybean ----------------
    "Soybean___healthy": {
        "title": "Healthy Soybean Foliage",
        "is_healthy": True,
        "description": "The soybean leaves exhibit normal trifoliate development with deep green color and no foliar lesions.",
        "recommendations": [
            "Monitor nodulation at root level to ensure effective biological nitrogen fixation.",
            "Ensure adequate soil phosphorus and potassium based on soil nutrient testing.",
            "Scout for soybean aphids and stink bugs during pod development stages."
        ],
        "prevention": [
            "Rotate crops annually with corn or small grains to suppress soybean cyst nematodes.",
            "Use certified inoculated seed suited for your maturity zone."
        ]
    },

    # ---------------- Squash ----------------
    "Squash___Powdery_mildew": {
        "title": "Squash Powdery Mildew (Podosphaera xanthii)",
        "is_healthy": False,
        "description": "A very common fungal disease creating dusty white powdery patches across leaf surfaces, causing premature yellowing and leaf death.",
        "recommendations": [
            "Apply potassium bicarbonate, sulfur, neem oil, or bio-fungicides at the first sign of white spots.",
            "Remove and discard heavily infected older crown leaves to slow fungal reproduction.",
            "Water exclusively at the base of the plant using drip or soaker hoses."
        ],
        "prevention": [
            "Select powdery mildew resistant squash and pumpkin cultivars.",
            "Space plants generously (at least 3 to 4 feet apart) to maximize air movement."
        ]
    },

    # ---------------- Strawberry ----------------
    "Strawberry___Leaf_scorch": {
        "title": "Strawberry Leaf Scorch (Diplocarpon earlianum)",
        "is_healthy": False,
        "description": "A fungal disease producing numerous small, irregular dark purple spots that enlarge and turn brown, giving foliage a scorched appearance.",
        "recommendations": [
            "Apply copper-based or captan fungicides if leaf scorch symptoms appear early in the season.",
            "Remove and dispose of severely spotted or dry, scorched leaves.",
            "Renovate strawberry beds after harvest by mowing foliage above the crown and clearing debris."
        ],
        "prevention": [
            "Plant certified disease-free strawberry runners in well-drained, raised beds.",
            "Avoid overhead irrigation to keep strawberry leaves and crowns dry."
        ]
    },
    "Strawberry___healthy": {
        "title": "Healthy Strawberry Foliage",
        "is_healthy": True,
        "description": "The strawberry plants are healthy, with bright green foliage and no signs of scorch, leaf spot, or botrytis rot.",
        "recommendations": [
            "Maintain 1 to 1.5 inches of water per week, especially during flowering and fruit ripening.",
            "Apply clean straw mulch beneath plants to keep ripening berries off bare soil.",
            "Fertilize with balanced organic berry food following the spring harvest."
        ],
        "prevention": [
            "Thin out crowded runners to maintain good spacing and sunlight penetration.",
            "Renovate June-bearing strawberry patches every 3 to 4 years to maintain vigor."
        ]
    },

    # ---------------- Tomato ----------------
    "Tomato___Bacterial_spot": {
        "title": "Tomato Bacterial Spot (Xanthomonas spp.)",
        "is_healthy": False,
        "description": "A bacterial disease causing small, dark, water-soaked leaf spots with yellow halos and raised scabby spots on tomato fruit.",
        "recommendations": [
            "Apply copper-based bactericides combined with mancozeb weekly during warm, rainy weather.",
            "Prune off lower infected foliage to reduce soil splash onto upper leaves.",
            "Avoid handling, pruning, or tying tomato plants when leaves are wet."
        ],
        "prevention": [
            "Use certified disease-free, hot-water treated seeds or resistant varieties.",
            "Use drip irrigation and mulch heavily under plants to prevent soil splashing."
        ]
    },
    "Tomato___Early_blight": {
        "title": "Tomato Early Blight (Alternaria linariae)",
        "is_healthy": False,
        "description": "A prevalent fungal disease causing dark brown lesions with concentric 'bullseye' rings, starting on lower mature leaves and progressing upward.",
        "recommendations": [
            "Prune off affected lower leaves up to 12 inches above the soil line.",
            "Apply protective fungicides (chlorothalonil, copper, or biofungicides like Bacillus subtilis).",
            "Water exclusively at soil level and avoid wetting the foliage."
        ],
        "prevention": [
            "Apply a 2-inch organic or plastic mulch layer to create a physical barrier against soil-borne spores.",
            "Practice a 3-year crop rotation with non-solanaceous crops (avoid potatoes, peppers, eggplants)."
        ]
    },
    "Tomato___Late_blight": {
        "title": "Tomato Late Blight (Phytophthora infestans)",
        "is_healthy": False,
        "description": "A rapid and devastating water mold creating large, greasy, dark lesions on leaves and stems with white fungal fuzz underneath in damp conditions.",
        "recommendations": [
            "Apply targeted systemic fungicides immediately if late blight is reported in your region.",
            "Immediately harvest remaining mature green fruit before infection reaches the stems.",
            "Remove and securely bag infected plants; do not compost late-blight infected plant tissue."
        ],
        "prevention": [
            "Plant resistant tomato cultivars (e.g., Defiant, Mountain Merit, Jasper, Plum Regal).",
            "Provide ample spacing (at least 2.5 to 3 feet) and stake or cage all tomato plants."
        ]
    },
    "Tomato___Leaf_Mold": {
        "title": "Tomato Leaf Mold (Passalora fulva)",
        "is_healthy": False,
        "description": "A fungal disease thriving in high humidity, producing pale yellow leaf spots on upper surfaces and olive-green velvety mold on the undersides.",
        "recommendations": [
            "Increase greenhouse or garden ventilation and reduce ambient relative humidity below 85%.",
            "Apply copper fungicides or biofungicides at the first detection of yellowing.",
            "Prune lower suckers and dense interior foliage to improve air circulation."
        ],
        "prevention": [
            "Grow leaf-mold resistant tomato hybrids in high tunnels and greenhouses.",
            "Space plants widely and avoid evening overhead watering."
        ]
    },
    "Tomato___Septoria_leaf_spot": {
        "title": "Tomato Septoria Leaf Spot (Septoria lycopersici)",
        "is_healthy": False,
        "description": "A common fungal disease causing numerous small, circular spots with gray centers and dark brown borders, speckled with tiny black specks.",
        "recommendations": [
            "Remove lower infected leaves as soon as spots appear to prevent upward spread.",
            "Apply organic copper or chlorothalonil fungicide every 7 to 10 days during rainy periods.",
            "Sterilize garden stakes and tomato cages with a 10% bleach solution between seasons."
        ],
        "prevention": [
            "Mulch the base of plants immediately after transplanting to prevent soil splash.",
            "Enforce a 3-year rotation away from all nightshade family crops."
        ]
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "title": "Tomato Two-Spotted Spider Mites (Tetranychus urticae)",
        "is_healthy": False,
        "description": "Microscopic sap-feeding arachnids causing fine yellow stippling, bronzed dry leaves, and fine silken webbing on leaf undersides during hot, dry weather.",
        "recommendations": [
            "Spray leaf undersides with insecticidal soap, neem oil, or rosemary oil sprays.",
            "Release natural biological predators such as Phytoseiulus persimilis predatory mites.",
            "Hose down dusty plant foliage with a strong jet of water to disrupt mite webbing."
        ],
        "prevention": [
            "Keep tomato plants well-hydrated; drought-stressed plants are significantly more vulnerable.",
            "Avoid broad-spectrum synthetic pyrethroids that eliminate natural spider mite predators."
        ]
    },
    "Tomato___Target_Spot": {
        "title": "Tomato Target Spot (Corynespora cassiicola)",
        "is_healthy": False,
        "description": "A fungal pathogen causing circular brown lesions with light brown centers and dark concentric rings on leaves, stems, and ripening fruit.",
        "recommendations": [
            "Apply protective fungicides (e.g., azoxystrobin, chlorothalonil, or copper) early.",
            "Prune diseased foliage and maintain stakes to elevate vines off the ground.",
            "Clear and discard all crop debris immediately following harvest."
        ],
        "prevention": [
            "Ensure wide plant spacing and regular staking for optimal airflow.",
            "Avoid overhead irrigation and overhead sprinkler splashing."
        ]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "title": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "is_healthy": False,
        "description": "A destructive viral pathogen transmitted by whiteflies, causing severe upward leaf curling, yellowing margins, stunted bushy growth, and flower drop.",
        "recommendations": [
            "Manage whitefly vectors using yellow sticky traps, insecticidal soaps, or systemic insecticides.",
            "Cover young seedlings with fine insect exclusion netting (mesh size < 0.25 mm).",
            "Immediately rogue out and destroy infected viral plants to protect surrounding crops."
        ],
        "prevention": [
            "Plant TYLCV-resistant tomato hybrids (e.g., Tycoon, Red Deuce, Charger).",
            "Eliminate broadleaf weeds around the garden perimeter that harbor whitefly populations."
        ]
    },
    "Tomato___Tomato_mosaic_virus": {
        "title": "Tomato Mosaic Virus (ToMV)",
        "is_healthy": False,
        "description": "A mechanically transmitted tobamovirus causing light and dark green mosaic mottling, leaf distortion ('shoestring' leaves), and internal fruit browning.",
        "recommendations": [
            "Carefully remove and destroy infected plants; do not compost virus-infected material.",
            "Wash hands thoroughly with soap or milk before handling healthy tomato plants.",
            "Disinfect all tools, stakes, and pruning shears in a 20% nonfat dry milk or bleach solution."
        ],
        "prevention": [
            "Plant certified virus-resistant varieties labeled with 'ToMV' or 'TMV'.",
            "Prohibit tobacco use near the garden (virus can be transmitted from tobacco products)."
        ]
    },
    "Tomato___healthy": {
        "title": "Healthy Tomato Foliage",
        "is_healthy": True,
        "description": "The tomato plant shows vigorous vegetative growth, deep green leaves, and no signs of fungal, bacterial, or viral disease.",
        "recommendations": [
            "Maintain deep, consistent watering (1.5 to 2 inches per week) to prevent blossom end rot and fruit splitting.",
            "Support plants with sturdy stakes, cages, or trellis lines to keep foliage off the ground.",
            "Apply balanced tomato fertilizer with micronutrients (calcium and magnesium) at first fruit set."
        ],
        "prevention": [
            "Mulch the soil surface with straw or wood shavings to maintain moisture and suppress weeds.",
            "Prune lower suckers to maintain single or double leader stems for optimal air circulation."
        ]
    }
}

DEFAULT_CAUTION = "Disclaimer: This recommendation is AI-assisted guidance based on image analysis and should be combined with on-site inspection. Consult local agricultural extension specialists before applying chemical treatments."

def get_recommendation(class_name: str) -> dict:
    """
    Returns structured disease recommendation and care advice for a given class name.
    Provides robust fallback if class is unrecognized.
    """
    if class_name in RECOMMENDATIONS:
        entry = RECOMMENDATIONS[class_name]
        return {
            "title": entry["title"],
            "is_healthy": entry.get("is_healthy", False),
            "description": entry["description"],
            "recommendations": entry["recommendations"],
            "prevention": entry["prevention"],
            "caution": DEFAULT_CAUTION
        }
    
    # Generic fallback
    is_healthy = "healthy" in class_name.lower()
    return {
        "title": class_name.replace("___", " - ").replace("_", " "),
        "is_healthy": is_healthy,
        "description": "The model classified this image, but specific customized guidance is not currently available in the database.",
        "recommendations": [
            "Monitor the plant closely for any progression or changes in leaf coloration.",
            "Ensure proper watering, balanced sunlight, and suitable soil drainage."
        ],
        "prevention": [
            "Maintain clean gardening tools and practice standard crop rotation.",
            "Consult a local plant nursery or agricultural extension officer for specific advice."
        ],
        "caution": DEFAULT_CAUTION
    }
