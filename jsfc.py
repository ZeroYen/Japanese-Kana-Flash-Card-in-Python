import pygame
import sys
import random

pygame.init()

# General rules
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NEW_FLASHCARD_EVENT = pygame.USEREVENT + 1

# Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Font with Japanese support
font = pygame.font.Font("MSMINCHO.TTF", 64)

# Kana dictionary
kana = {
    'hiragana': {
        'あ': 'a',
        'い': 'i',
        'う': 'u',
        'え': 'e',
        'お': 'o',
        'か': 'ka',
        'き': 'ki',
        'く': 'ku',
        'け': 'ke',
        'こ': 'ko',
        'さ': 'sa',
        'し': 'shi',
        'す': 'su',
        'せ': 'se',
        'そ': 'so',
        'た': 'ta',
        'ち': 'chi',
        'つ': 'tsu',
        'て': 'te',
        'と': 'to',
        'な': 'na',
        'に': 'ni',
        'ぬ': 'nu',
        'ね': 'ne',
        'の': 'no',
        'は': 'ha',
        'ひ': 'hi',
        'ふ': 'fu',
        'へ': 'he',
        'ほ': 'ho',
        'ま': 'ma',
        'み': 'mi',
        'む': 'mu',
        'め': 'me',
        'も': 'mo',
        'や': 'ya',
        'ゆ': 'yu',
        'よ': 'yo',
        'ら': 'ra',
        'り': 'ri',
        'る': 'ru',
        'れ': 're',
        'ろ': 'ro',
        'わ': 'wa',
        'を': 'wo',
        'ん': 'n',
        'が': 'ga',
        'ぎ': 'gi',
        'ぐ': 'gu',
        'げ': 'ge',
        'ご': 'go',
        'ざ': 'za',
        'じ': 'ji',
        'ず': 'zu',
        'ぜ': 'ze',
        'ぞ': 'zo',
        'だ': 'da',
        'ぢ': 'ji',
        'づ': 'zu',
        'で': 'de',
        'ど': 'do',
        'ば': 'ba',
        'び': 'bi',
        'ぶ': 'bu',
        'べ': 'be',
        'ぼ': 'bo',
        'ぱ': 'pa',
        'ぴ': 'pi',
        'ぷ': 'pu',
        'ぺ': 'pe',
        'ぽ': 'po',
        'きゃ': 'kya',
        'きゅ': 'kyu',
        'きょ': 'kyo',
        'ぎゃ': 'gya',
        'ぎゅ': 'gyu',
        'ぎょ': 'gyo',
        'しゃ': 'sha',
        'しゅ': 'shu',
        'しょ': 'sho',
        'じゃ': 'ja',
        'じゅ': 'ju',
        'じょ': 'jo',
        'ちゃ': 'cha',
        'ちゅ': 'chu',
        'ちょ': 'cho',
        'にゃ': 'nya',
        'にゅ': 'nyu',
        'にょ': 'nyo',
        'ひゃ': 'hya',
        'ひゅ': 'hyu',
        'ひょ': 'hyo',
        'びゃ': 'bya',
        'びゅ': 'byu',
        'びょ': 'byo',
        'ぴゃ': 'pya',
        'ぴゅ': 'pyu',
        'ぴょ': 'pyo',
        'みゃ': 'mya',
        'みゅ': 'myu',
        'みょ': 'myo',
        'りゃ': 'rya',
        'りゅ': 'ryu',
        'りょ': 'ryo',
    },
    'katakana': {
        'ア': 'a',
        'イ': 'i',
        'ウ': 'u',
        'エ': 'e',
        'オ': 'o',
        'カ': 'ka',
        'キ': 'ki',
        'ク': 'ku',
        'ケ': 'ke',
        'コ': 'ko',
        'サ': 'sa',
        'シ': 'shi',
        'ス': 'su',
        'セ': 'se',
        'ソ': 'so',
        'タ': 'ta',
        'チ': 'chi',
        'ツ': 'tsu',
        'テ': 'te',
        'ト': 'to',
        'ナ': 'na',
        'ニ': 'ni',
        'ヌ': 'nu',
        'ネ': 'ne',
        'ノ': 'no',
        'ハ': 'ha',
        'ヒ': 'hi',
        'フ': 'fu',
        'ヘ': 'he',
        'ホ': 'ho',
        'マ': 'ma',
        'ミ': 'mi',
        'ム': 'mu',
        'メ': 'me',
        'モ': 'mo',
        'ヤ': 'ya',
        'ユ': 'yu',
        'ヨ': 'yo',
        'ラ': 'ra',
        'リ': 'ri',
        'ル': 'ru',
        'レ': 're',
        'ロ': 'ro',
        'ワ': 'wa',
        'ヲ': 'wo',
        'ン': 'n',
        'ガ': 'ga',
        'ギ': 'gi',
        'グ': 'gu',
        'ゲ': 'ge',
        'ゴ': 'go',
        'ザ': 'za',
        'ジ': 'ji',
        'ズ': 'zu',
        'ゼ': 'ze',
        'ゾ': 'zo',
        'ダ': 'da',
        'ヂ': 'ji',
        'ヅ': 'zu',
        'デ': 'de',
        'ド': 'do',
        'バ': 'ba',
        'ビ': 'bi',
        'ブ': 'bu',
        'ベ': 'be',
        'ボ': 'bo',
        'パ': 'pa',
        'ピ': 'pi',
        'プ': 'pu',
        'ペ': 'pe',
        'ポ': 'po',
        'キャ': 'kya',
        'キュ': 'kyu',
        'キョ': 'kyo',
        'ギャ': 'gya',
        'ギュ': 'gyu',
        'ギョ': 'gyo',
        'シャ': 'sha',
        'シュ': 'shu',
        'ショ': 'sho',
        'ジャ': 'ja',
        'ジュ': 'ju',
        'ジョ': 'jo',
        'チャ': 'cha',
        'チュ': 'chu',
        'チョ': 'cho',
        'ニャ': 'nya',
        'ニュ': 'nyu',
        'ニョ': 'nyo',
        'ヒャ': 'hya',
        'ヒュ': 'hyu',
        'ヒョ': 'hyo',
        'ビャ': 'bya',
        'ビュ': 'byu',
        'ビョ': 'byo',
        'ピャ': 'pya',
        'ピュ': 'pyu',
        'ピョ': 'pyo',
        'ミャ': 'mya',
        'ミュ': 'myu',
        'ミョ': 'myo',
        'リャ': 'rya',
        'リュ': 'ryu',
        'リョ': 'ryo',
    },
}

# List of all the Japanese characters
characters = list(kana['hiragana'].items()) + list(kana['katakana'].items())

# Timer set to 3 seconds
pygame.time.set_timer(NEW_FLASHCARD_EVENT, 3000)

# Randomizer
character, pronunciation = random.choice(characters)

# Rendering text onto screen
text = font.render(f"{character}/{pronunciation}", True, WHITE)
text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

# Author
author_font = pygame.font.Font(None, 18)
author_text = author_font.render("David Kamaly", True, WHITE)
author_text_rect = author_text.get_rect(bottomright=(SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == NEW_FLASHCARD_EVENT:
            character, pronunciation = random.choice(characters)
            text = font.render(f"{character}/{pronunciation}", True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    screen.fill(BLACK)
    screen.blit(text, text_rect)
    screen.blit(author_text, author_text_rect)
    pygame.display.flip()
