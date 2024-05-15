from flask import Flask, render_template
from sessao import Sessao
from comentario import Comentario
from palestrante import Palestrante

app = Flask(__name__)

palestrante_Heloisa=Palestrante(1,"Heloisa", "Software Engineer",'https://media.licdn.com/dms/image/D4D03AQErleKHDYzqxA/profile-displayphoto-shrink_800_800/0/1706621108214?e=2147483647&v=beta&t=NTYzygJdXwTXCSz2D565tga38Bqe2ZUcypzJyPSmpzQ', "Olá, sou Heloisa Cabral, graduanda do curso de engenharia de software pela Universidade de Vassouras, com 3 anos de experiência em front-end, trabalhando com JavaScript, React, Node, HTML e CSS. Trabalhei principalmente no setor de inovação e novos negócios, onde fui responsável pelo desenvolvimento de projetos para a comunidade interna. Estou no caminho para me formar como engenheira de software e possuo certificação internacional de proficiência na língua inglesa. Minha paixão é utilizar da tecnologia para automatizar processos do cotidiano, e é por isso que dei entrada na minha iniciação científica com um projeto de chatbot para ajudar setores administrativos da universidade em que estudo. Atualmente sou Software Engineer Intern na DMS Logistics, onde trabalho principalmente com Linux, Docker, Postgresql, Django e React.", "https://br.linkedin.com/in/heloisa-cabral-4a112b248")
comentario_bernardo=Comentario(1, "Bernardo", "A melhor das melhores que há.", "16h20min")
sessao_gemini=Sessao(1, "7213", "Utilização do Gemini no nosso cotidiano", "20h00min", "Null")

@app.route("/")
def home():
    return render_template("index.html")