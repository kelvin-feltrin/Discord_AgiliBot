import discord

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'Hello world!'
    
    if p_message == '!ping':
        return 'pong'
    
    if p_message == '!pong':
        return 'ping'

    if p_message.startswith('!livro'):
        text_params = message.replace('!livro', '')
        params_list = text_params.split(';')

        if len(params_list) == 4:
            title = params_list[0]
            author = params_list[1]
            category = params_list[2]
            link = params_list[3]

            message_formatted = f'📚 | **Título:** {title} \n\n✍️ | **Autor:** {author} \n\n📌 | **Categoria:** {category} \n\n🔗 | **Link:** {link}'

            return message_formatted
        else:
            return 'Comando inválido! Digite `!livro titulo; autor; categoria; link`'

    if p_message.startswith('!comando'):
        return 'Para ver a lista de comandos acesse: <https://github.com/kelvin-feltrin/Discord_AgiliBot/tree/main#readme>'