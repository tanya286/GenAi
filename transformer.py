from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("The sanctions bill comes at a time when India's dependence on Russian energy has increased due to the West Asia war, which has disrupted shipping through the Strait of Hormuz. The Iran-US war has choked off Gulf crude supplies that previously accounted for roughly 40 percent of India's oil imports, forcing refiners to turn to Russian crude as the main alternative source.")

print(result)