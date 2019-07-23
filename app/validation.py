"""
Descriptif de la tache:
Faire une fonction w3c_validation qui permet de valider un code html

@param {str} : le code w3c à valider
@return {dic} : une clé score qui contient un int et une clé erreurs qui contient les résultats des erreurs.
"""
import requests
from bs4 import BeautifulSoup


HTMLcode = """
<html>
  <head>
    <title>test swup</title>
    <meta content="">
<script src="./dist/swup.js"></script>
<link rel="stylesheet" href="style.css">

  </head>
  <body>
    <div class="partie-fix">
        
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Harum ipsum modi est nisi sint voluptatem sapiente atque, autem magni. Quas quasi laudantium non eveniet amet, praesentium soluta reprehenderit voluptates. Alias!
            
            <div id="swup" class="blue animation-class transition-fade">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut, commodi, rerum. Corrupti architecto eos cumque quod aliquid, eaque eligendi facere non maiores blanditiis, perferendis perspiciatis quia enim ea commodi, illo?
            </div>
    
    </div>
    <a href="index.html">lien vers page d'accueil</a>
    <a href="page2.html">lien vers page 2</a>
    <script>
let options = {
    animations: {
        '*': {
            in: function(next){
                document.querySelector('#swup').style.opacity = 0;
                TweenLite.to(document.querySelector('#swup'), .5, {
                    opacity: 1,
                    onComplete: next
                });
            },
            out: function(next){
                document.querySelector('#swup').style.opacity = 1;
                TweenLite.to(document.querySelector('#swup'), .5, {
                    opacity: 0,
                    onComplete: next
                });
            }
        },
    }
}

const swupjs = new Swupjs(options);
</script>
  </body>
</html>
"""


def w3c_validation(HTMLcode):
    """
    Valider un code html avec w3c validator
    et renvoie la réponse HTML du formulaire

    @param {str} : le code w3c à valider
    @return {resquest.reponse} : une clé score qui contient un int et une clé erreurs qui contient les résultats des erreurs.
    
    #ToDo : utiliser l'api json au lieu de la réponse HTML
    """
  
    url = "https://validator.w3.org/nu/"
    b_HTMLcode = bytes(HTMLcode, 'utf-8')
    print(b_HTMLcode)
    print(type(b_HTMLcode))
    files =  {"file":("code" ,b_HTMLcode,None,None )} 
    r = requests.post(url,files=files )
    # r2 = requests.post(url_2 )
    return r


def parser_w3c_result(reponseHTML):
    """
    Récupère les class "warning" et "error"
    de la réponse du w3c validateur

    @param 
    """
    soup = BeautifulSoup(reponseHTML.text, 'html.parser')
    errors = soup.find_all(class_="error")
    warnings = soup.find_all(class_="warning")
    error_items = []
    warning_items = []
    for error in errors:
        error_items.append(error.find('span'))
    for warning in warnings:
        warning_items.append(warning.find('span'))
    print(error_items)
    print(len(error_items))
    print(warning_items)
    print(len(warning_items))


if __name__ == '__main__':
    r = w3c_validation(HTMLcode)
    parser_w3c_result(r)