import csv 

offensive = "Macaco; seu macaco; seu preto; yasuo lixo toxico podre; comi sua mãe; \
    não foi o que sua mae disse ontem; primeiro macaco que vejo jogando lol; se mata; \
    enfia um poste no cu; vai se foder seu anão de merda; porque voce não atira no proprio cu; \
    sua mãe devia te abortar; quer que eu mande link da corda no mercado livre?;\
    nunca vi uma doença tão grande jogando lol; um dia Deus falou que ia acabar com o mundo ai voce nasceu;\
    sua mãe tem orgulho da merda que ela cagou no mundo; preto; macaco; carvão; escuro; \
    chris só que negro; resto de palha queimada; nazista; hittler tava certo; judeu de merda; \
    que deus te elimine; vai se foder; imbecil; panaca; lugar de mulher é na cozinha; vai dar o cu; \
    mulher só serve pra dar; seu pai deu o cu pra um anão; pau no seu cu; porque vc n se mata?; doença em pessoa; anão do pé torto; \
    esquizofrenico sem amigos; doença em pessoa; compra uma corda e vai jogar no vasco; \
    sexo com morto é mais gostoso; comi sua mãe; jesus se matou depois de conhecer sua mãe, panaca; \
    doença; corona virus em pessoa; peste negra em cor; falta de tapa na cara; sua mãe sentou torto; \
    nasceu esse groot; cadeirante ciclista; sua mãe transou com um javali e tu nasceu; \
    aborto não existia no seu tempo pois vc ta vivo ainda; se mata imbecil;\
    vai cherar um litro de coca; onde ja se viu preto com direito de fala?;\
    Se acha vitorioso só por que sobreviveu a um aborto; vai se fuder; nao merece a vida; \
    se mata; horrivel; fudido; arrombado; vai tomar no cu; aborto; Seu viado, jogador de Lulu; \
    Tinha que ser preto e pobre pra tá com computador travando o inicio da partida;\
    Você é um retardado por está jogando dessa maneira; fudido do caralho;\
    jogador lixo do caralho; verme;  tinha que ser pobre; preto carvao; vagabundo; nao tem oq fazer da vida?;\
    que jogo lixo; vc devia se matar; Macaco; viado; nordestino; baiano;\
    fudido; preto safado ; pau no cu; se mata; verme; Você é um lixo; veado;\
    cara você é horrível; lixo; inútil; um bosta;  mongoloide; vc é um merda; \
    filho da puta; se mata; macaco; Horroroso; imundo; Tu é mais feio que pedófilo anão;\
    Tua mãe; Vai lixo; Teu cu;arrombado de merda; lixo humano; pq tu nao se mata; parece um macaco;\
    chimpanzé; primata; seu gorila; seu africano;deveria desinstalar, seu merda; burro;\
    imbecil; otario; tinha que ser preto; fraco; desempregado; horriveis; podres;Macaco; parasita;\
    Vagabunda; baiano; vai lavar prato; gorda; salario mínimo; Energúmena; acéfalo;\
    se mata; ruim, tomara que morra; Adotado;filho do matue; cearense cabeça de orelhão;\
    filho da puta; sequelado; desgraçado; desinstala o jogo; não sabe jogar; burro; tua mãe;\
    horrível; Se mata favelado; volta pra senzala macaco; Burro; Idiota; Animal; Acéfalo; quero que voce se foda"

non_offensive = "wp time; boa; joga muito; nice; fez o basico; bom jogo;boa;jogou muito; caraca; o que foi isso?;\
    Esse cara é muito bom; gostoso; jogou muito; parabens; que cara bom; deita e rola; kkkkkk; kkkk; kkk; \
    como vc esta?; espera; to chegando; vou gankar; vamo top; to bem; vou fzr azul; roubei; vamo dragao; vamo dg;\
    Não liga para essas pessoas que só querem o mal, apenas mute e siga se divertindo; Você é uma ótima pessoa é tá jogando bem;\
    não precisa ficar mal com tantas mensagens ofensivas; Parabéns por joga bem diferente de tudo que estão falando;\
    booaa; que foi issooo;linda play; me salvou; obrigado; parabens por ser tao bom; boaaaa mlkk , joga mt, quer ser meu padrasto?;\
    Você joga bem; Boa; é isso ai; jogou o fino; nice; boa; a culpa foi minha, sorry; Boa; Jogou mt c eh loko; Humilde;boa mano; \
    lindo dms; jogador caro; gostoso; jogou bem; gg wp; parem de discutir e comecem a jogar, irei mutar todos para não me estressar;\
    Boa jogada; Salvou o time; Carregou; Tudo bem errar;Jogou bem;ggwp;vou copiar sua build;jogou bem; boa; Lindao;queria mais 3 de tu no meu time;\
    Vamos conseguir ganhar; Bom jogo; tu é muito bom; obrigado por existir; deus na terra; po, valeu ai; vamo duo ?; \
    que cara bom; é smurf certeza; parabens; perfeito; boa krl; nice; bouaa; jogou o fino; jogou; mec; god; diferenciado; \
    bonecao; game nosso; tudo nosso; gameplay avançada; Deus; é o grongos; fala dele; arrebentou; ganhou solo; carregou;\
    é main; quem te ensinou?; relaxa; seu lindo; liga nao; respira time; confia; calmou; mito; destruiu; genio; humilde; jogou muito;\
    high elo; sou foda; muito forte; cara voce é muito bom; well played; show; insano; show de bola; embrasado; me carrega; desculpa;\
    malz ae; como tu fez isso?; kkkkk, essa foi boa; frenetico; salvou; concordo ctg; bora time; time dos sonhos; vamo q vamo;\
    show de bola; tranquilo; beleza; claro; boa noite; bom dia; boa tarde; me beija; gato; gata; gatinha; sucesso; glhf; meu rei;\
    rainha; vamo com calma; alegria; bonecao"

offensive = offensive.lower()
non_offensive = non_offensive.lower()

data_offensive = offensive.split(";")
data_non_offensive = non_offensive.split(";")

print(len(data_offensive))
print(len(data_non_offensive))



with open('data.csv', 'w',  encoding='utf-8', newline='') as file:
    
    writer = csv.writer(file)
    for i in range(len(data_offensive)):
        writer.writerow([data_offensive[i], 1])
        writer.writerow([data_non_offensive[i], 0])

