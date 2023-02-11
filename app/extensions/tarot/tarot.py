import discord
from tarot_data import tarotData
import random

#Stealing this for the decorator in the main commands module.
#@client.hybrid_command(brief='Single card tarot draw', help='Draws a random card from a 78 card Rider-Waite tarot deck, including reversed cards.')
async def tarot(ctx):
    if '__template' in tarotData:
        await ctx.send('Oops, someone needs to put a proper tarot deck into my brain first!')
    else:
        if 'deck' in tarotData:
            card_index = random.randint(0, len(tarotData['deck'])-1)
            card = tarotData['deck'][card_index]
            emb = discord.Embed(type='rich', title=card['title'], description=card['meaning'], url=card['url'])
            emb.add_field(name='Keywords', value=', '.join(card['keywords']) )
            emb.add_field(name='Yes/No?', value=card['yesno'])
            emb.set_image(url=card['image'])
            emb.set_footer(text='Images © Labyrinthos LLC')
            await ctx.send('{0.display_name}, you have drawn: '.format(ctx.message.author), embed=emb)
        else:
            await ctx.send('Oops, I do not seem to have a valid tarot deck loaded, sorry!')