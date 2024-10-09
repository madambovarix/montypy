import scrapy
import re

class MontyPythonSpider(scrapy.Spider):
    name = 'montypython'
    start_urls = ['https://www.ibras.dk/montypython/mainlist.htm']
    
    def parse(self, response):
        episode_links = response.css('a[href*="episode"]::attr(href)').getall()
        for link in episode_links:
            absolute_link = response.urljoin(link)
            yield scrapy.Request(absolute_link, callback=self.parse_episode)
    
    def parse_episode(self, response):
        title = response.css('h1::text').get() or response.css('title::text').get()
        
        # Extraction du script
        script = []
        current_scene = {"description": "", "dialogue": []}
        
        # Parcourir toutes les lignes de la table
        for row in response.css('tr'):
            # Extraire le texte de la ligne, qu'il soit direct ou dans une balise font
            texts = row.css('td::text, td font::text').getall()
            texts = [t.strip() for t in texts if t.strip()]
            
            if not texts:
                continue
            
            # Identifier le type de ligne
            if all(t.isupper() for t in texts):
                # C'est probablement un en-tête de scène
                if current_scene["dialogue"]:
                    script.append(current_scene)
                    current_scene = {"description": "", "dialogue": []}
                current_scene["description"] = " ".join(texts)
            elif len(texts) >= 2:
                # C'est probablement un dialogue
                speaker = texts[0]
                text = " ".join(texts[1:])
                if not re.match(r'^[\[\(\{].*[\]\)\}]$', text):  # Ignorer les directions scéniques
                    current_scene["dialogue"].append({
                        "speaker": speaker,
                        "text": text
                    })
            else:
                # C'est peut-être une direction scénique
                stage_direction = texts[0]
                if not current_scene["description"]:
                    current_scene["description"] = stage_direction
                else:
                    current_scene["dialogue"].append({
                        "speaker": "",
                        "stage_direction": stage_direction
                    })
        
        # N'oubliez pas la dernière scène
        if current_scene["dialogue"]:
            script.append(current_scene)
        
        # Extraction des annotations (texte en italique)
        annotations = response.css('i::text').getall()
        
        yield {
            'episode_number': re.search(r'Episode (\d+)', title).group(1) if re.search(r'Episode (\d+)', title) else None,
            'title': title,
            'url': response.url,
            'script': script,
            'annotations': annotations
        }
    
    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'MontyPythonBot (Educational Project)',
        'DOWNLOAD_DELAY': 1,
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEEDS': {
            'monty_python_scripts.json': {
                'format': 'json',
                'indent': 2,  # Pour un JSON bien formaté
                'ensure_ascii': False,  # Pour gérer correctement les caractères non-ASCII
            }
        }
    }

# Instructions d'exécution :
# 1. Créer un nouveau projet Scrapy
# 2. Copier ce script dans le fichier spider
# 3. Exécuter : scrapy crawl montypython -o monty_python_scripts.json