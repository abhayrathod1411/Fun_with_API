from simple_colors import *
def simple_colors():
    # normal and colored text
    print('Normal:', blue('Welcome Finxter!'))
    # print BOLD and colored text
    print('BOLD: ', green('Welcome Finxter!', 'bold'))
    # print BOLD and Underlined and colored text
    print('BOLD and Underlined: ', red('Welcome Finxter!', ['bold', 'underlined']))


def prompt_toolkit():
    from prompt_toolkit import print_formatted_text, HTML
    from prompt_toolkit.styles import Style
    sty = Style.from_dict({
        'y': '#44ff00 bold ',
    })
    print_formatted_text (HTML('<y> Hello and welcome to <u>Finxter!</u> </y>'), style=sty)

def prompt_pygments():
    from pygments.token import Token
    from prompt_toolkit import print_formatted_text
    from prompt_toolkit.formatted_text import PygmentsTokens

    text = [
        (Token.Keyword, 'print'),
        (Token.Punctuation, '('),
        (Token.Literal.String.Double, '"'),
        (Token.Literal.String.Double, 'hello'),
        (Token.Literal.String.Double, '"'),
        (Token.Punctuation, ')'),
        (Token.Text, '\n'),
    ]

    print_formatted_text(PygmentsTokens(text))

prompt_toolkit()