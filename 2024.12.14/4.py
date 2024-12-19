from pathlib import Path
import pymorphy2
from utils import remove_punctuation
from pprint import pprint

def search_context(keyword, *keywords, n = 0):

    text = []
    keys = [keyword] + list(keywords)
    morph = pymorphy2.MorphAnalyzer()
    
    keywordlemmas = {kw: morph.parse(kw)[0].normal_form for kw in keys}
    
    path = Path(r'C:\data scientist\Pautina\2024.12.14\data')
    for file in path.glob('*.txt'):
        with open(file, 'r', encoding='utf-8') as file_txt:
            lines = file_txt.readlines()
        
        for line_num, line in enumerate(lines, start=1):
            line = remove_punctuation(line)
            for word in line.split():
                initial_form = morph.parse(word)[0].normal_form
                
                if initial_form in keywordlemmas.values():
                    start = max(0, line_num - n - 1)
                    end = min(len(lines), line_num + n)
                    context = ''.join(lines[start:end]).strip()
                    
                    text.append({
                        'context': context,
                        'filename': file.name,
                        'linenumber': line_num,
                        'keyword': initial_form
                    })

    return text

#>>> pprint(search_context('мысль', 'мысли'))
#[{'context': '- А знаете, Павел Иванович, - сказал Манилов, которому очень '
#             'понравилась такая мысль, - как было бы в самом деле хорошо, если '
#             'бы жить этак вместе, под одною кровлею, или под тенью '
#             'какого-нибудь вяза пофилософствовать о чем-нибудь, углубиться!..',
#  'filename': 'E3ln1.txt',
#  'keyword': 'мысль',
#  'linenumber': 147},
# {'context': 'Манилов долго стоял на крыльце, провожая глазами удалявшуюся '
#             'бричку, и когда она уже совершенно стала не видна, он все еще '
#             'стоял, куря трубку. Наконец вошел он в комнату, сел на стуле и '
#             'предался размышлению, душевно радуясь, что доставил гостю своему '
#             'небольшое удовольствие. Потом мысли его перенеслись незаметно к '
#             'другим предметам и наконец занеслись бог знает куда. Он думал о '
#             'благополучии дружеской жизни, о том, как бы хорошо было жить с '
#             'другом на берегу какой-нибудь реки, потом чрез эту реку начал '
#             'строиться у него мост, потом огромнейший дом с таким высоким '
#             'бельведером, что можно оттуда видеть даже Москву, и там пить '
#             'вечером чай на открытом воздухе и рассуждать о каких-нибудь '
#             'приятных предметах. Потом, что они вместе с Чичиковым приехали в '
#             'какое-то общество в хороших каретах, где обворожают всех '
#             'приятностию обращения, и что будто бы государь, узнавши о такой '
#             'их дружбе, пожаловал их генералами, и далее, наконец, бог знает '
#             'что такое, чего уже он и сам никак не мог разобрать. Странная '
#             'просьба Чичикова прервала вдруг все его мечтания. Мысль о ней '
#             'как-то особенно не варилась в его голове: как ни переворачивал '
#             'он ее, но никак не мог изъяснить себе, и все время сидел он и '
#             'курил трубку, что тянулось до самого ужина.',
#  'filename': 'E3ln1.txt',
#  'keyword': 'мысль',
#  'linenumber': 163},
# {'context': 'Манилов долго стоял на крыльце, провожая глазами удалявшуюся '
#             'бричку, и когда она уже совершенно стала не видна, он все еще '
#             'стоял, куря трубку. Наконец вошел он в комнату, сел на стуле и '
#             'предался размышлению, душевно радуясь, что доставил гостю своему '
#             'небольшое удовольствие. Потом мысли его перенеслись незаметно к '
#             'другим предметам и наконец занеслись бог знает куда. Он думал о '
#             'благополучии дружеской жизни, о том, как бы хорошо было жить с '
#             'другом на берегу какой-нибудь реки, потом чрез эту реку начал '
#             'строиться у него мост, потом огромнейший дом с таким высоким '
#             'бельведером, что можно оттуда видеть даже Москву, и там пить '
#             'вечером чай на открытом воздухе и рассуждать о каких-нибудь '
#             'приятных предметах. Потом, что они вместе с Чичиковым приехали в '
#             'какое-то общество в хороших каретах, где обворожают всех '
#             'приятностию обращения, и что будто бы государь, узнавши о такой '
#             'их дружбе, пожаловал их генералами, и далее, наконец, бог знает '
#             'что такое, чего уже он и сам никак не мог разобрать. Странная '
#             'просьба Чичикова прервала вдруг все его мечтания. Мысль о ней '
#             'как-то особенно не варилась в его голове: как ни переворачивал '
#             'он ее, но никак не мог изъяснить себе, и все время сидел он и '
#             'курил трубку, что тянулось до самого ужина.',
#  'filename': 'E3ln1.txt',
#  'keyword': 'мысль',
#  'linenumber': 163},
# {'context': 'Как и все старые люди вообще, графиня страдала бессонницею. '
#             'Раздевшись, она села у окна в вольтеровы кресла и отослала '
#             'горничных. Свечи вынесли, комната опять осветилась одною '
#             'лампадою. Графиня сидела вся желтая, шевеля отвислыми губами, '
#             'качаясь направо и налево. В мутных глазах ее изображалось '
#             'совершенное отсутствие мысли; смотря на нее, можно было бы '
#             'подумать, что качание страшной старухи происходило не от ее '
#             'воли, но по действию скрытого гальванизма.',
#  'filename': 'le1UO.txt',
#  'keyword': 'мысль',
#  'linenumber': 13},
# {'context': '…А любопытно, однако ж, для чего мамаша о «новейших-то '
#             'поколениях» мне написала? Просто ли для характеристики лица или '
#             'с дальнейшею целью: задобрить меня в пользу господина Лужина? О, '
#             'хитрые! Любопытно бы разъяснить еще одно обстоятельство: до '
#             'какой степени они обе были откровенны друг с дружкой в тот день '
#             'и в ту ночь и во все последующее время? Все ли слова между ними '
#             'были прямо произнесены или обе поняли, что у той и у другой одно '
#             'в сердце и в мыслях, так уж нечего вслух-то всего выговаривать '
#             'да напрасно проговариваться. Вероятно, оно так отчасти и было; '
#             'по письму видно: мамаше он показался резок, немножко, а наивная '
#             'мамаша и полезла к Дуне с своими замечаниями. А та, разумеется, '
#             'рассердилась и «отвечала с досадой».',
#  'filename': 'r62Bf.txt',
#  'keyword': 'мысль',
#  'linenumber': 4},
# {'context': '«Гм, это правда, - продолжал он, следуя за вихрем мыслей, '
#             'крутившимся в его голове, - это правда, что к человеку надо '
#             '«подходить постепенно и осторожно, чтобы разузнать его»; но '
#             'господин Лужин ясен. Главное, «человек деловой и, кажется, '
#             'добрый»: шутка ли, поклажу взял на себя, большой сундук на свой '
#             'счет доставляет! Ну, как же не добрый? А они-то обе, невеста и '
#             'мать, мужичка подряжают, в телеге, рогожею крытой (я ведь так '
#             'езжал)! Ничего! Только ведь девяносто верст, «а там '
#             'преблагополучно прокатимся в третьем классе», верст тысячу. И '
#             'благоразумно: по одежке протягивай ножки; да вы то, г-н Лужин, '
#             'чего же? Ведь это ваша невеста… И не могли же вы не знать, что '
#             'мать под свой пенсион на дорогу вперед занимает? Конечно, тут у '
#             'вас общий коммерческий оборот, предприятие на обоюдных выгодах и '
#             'на равных паях, значит, и расходы пополам; хлеб-соль вместе, а '
#             'табачок врозь, по пословице. Да и тут деловой-то человек их '
#             'поднадул немножко: поклажа-то стоит дешевле ихнего проезда, а, '
#             'пожалуй, что и задаром пойдет.',
#  'filename': 'r62Bf.txt',
#  'keyword': 'мысль',
#  'linenumber': 6},
# {'context': 'Вдруг он вздрогнул: одна, тоже вчерашняя, мысль опять пронеслась '
#             'в его голове. Но вздрогнул он не оттого, что пронеслась эта '
#             'мысль. Он ведь знал, он предчувствовал, что она непременно '
#             '«пронесется», и уже ждал ее; да и мысль эта была совсем не '
#             'вчерашняя. Но разница была в том, что месяц назад, и даже вчера '
#             'еще, она была только мечтой, а теперь… теперь явилась вдруг не '
#             'мечтой, а в каком-то новом, грозном и совсем незнакомом ему '
#             'виде, и он вдруг сам сознал это… Ему стукнуло в голову, и '
#             'потемнело в глазах.',
#  'filename': 'r62Bf.txt',
#  'keyword': 'мысль',
#  'linenumber': 19},
# {'context': 'Вдруг он вздрогнул: одна, тоже вчерашняя, мысль опять пронеслась '
#             'в его голове. Но вздрогнул он не оттого, что пронеслась эта '
#             'мысль. Он ведь знал, он предчувствовал, что она непременно '
#             '«пронесется», и уже ждал ее; да и мысль эта была совсем не '
#             'вчерашняя. Но разница была в том, что месяц назад, и даже вчера '
#             'еще, она была только мечтой, а теперь… теперь явилась вдруг не '
#             'мечтой, а в каком-то новом, грозном и совсем незнакомом ему '
#             'виде, и он вдруг сам сознал это… Ему стукнуло в голову, и '
#             'потемнело в глазах.',
#  'filename': 'r62Bf.txt',
#  'keyword': 'мысль',
#  'linenumber': 19},
# {'context': 'Вдруг он вздрогнул: одна, тоже вчерашняя, мысль опять пронеслась '
#             'в его голове. Но вздрогнул он не оттого, что пронеслась эта '
#             'мысль. Он ведь знал, он предчувствовал, что она непременно '
#             '«пронесется», и уже ждал ее; да и мысль эта была совсем не '
#             'вчерашняя. Но разница была в том, что месяц назад, и даже вчера '
#             'еще, она была только мечтой, а теперь… теперь явилась вдруг не '
#             'мечтой, а в каком-то новом, грозном и совсем незнакомом ему '
#             'виде, и он вдруг сам сознал это… Ему стукнуло в голову, и '
#             'потемнело в глазах.',
#  'filename': 'r62Bf.txt',
#  'keyword': 'мысль',
#  'linenumber': 19},
# {'context': 'Несмотря на эти странные слова, ему стало очень тяжело. Он '
#             'присел на оставленную скамью. Мысли его были рассеянны… Да и '
#             'вообще тяжело ему было думать в эту минуту о чем бы то ни было. '
#             'Он бы хотел совсем забыться, все забыть, потом проснуться и '
#             'начать совсем сызнова…',
#  'filename': 'r62Bf.txt',
#  'keyword': 'мысль',
#  'linenumber': 61},
# {'context': '«А куда ж я иду? - подумал он вдруг. - Странно. Ведь я зачем-то '
#             'пошел. Как письмо прочел, так и пошел… На Васильевский остров, к '
#             'Разумихину я пошел, вот куда, теперь… помню. Да зачем, однако '
#             'же? И каким образом мысль идти к Разумихину залетела мне именно '
#             'теперь в голову? Это замечательно».',
#  'filename': 'r62Bf.txt',
#  'keyword': 'мысль',
#  'linenumber': 63}]
#