from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

default_lang = "en"

prefix = ["/", "!", "#", "."]


start_message_text = """
**Hello {}, I am TranslatorBot \ud83e\udd16

  I can translate any language to you selected language, just send me something.\n\n🏷️ Maintained By:@Amani_m_h_d**

**Available commands:
/help - Show this help message
/language - Set your main language**

__Enjoy! ☺__"""

start_message_reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔍 Inline here", switch_inline_query_current_chat=" "),
        ],
        [
            InlineKeyboardButton("💡 Help", callback_data="help"),
        ],
    ]
)

help_markup = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🔙 Back", callback_data="back")],
    ]
)

error_message_markup = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🗑 Delete this message", callback_data="closethismsg")],
    ]
)



help_text = """
**Simple Translate Bot**

 `A bot to help you translate text (with emojis) to few Languages from any other language.`

**How To**
**Just send copied text or forward message with other language to Translator Bot and you'll receive a translation of the message in the language of your choice. Send /language command to know which language is available.**

****More help****

**Groups**
/tr (language) by reply to translate the replied message

**Translate in private chat without change the main language**
/tr (language) (text)

**Translate in inline mode**
@TG_translatorbot (language) (text)

"""

language_text = """
**Languages**

__Select the language you want to translate.__

•/lang (language code) 

Example: ```/lang en``` 

List of language codes: https://cloud.google.com/translate/docs/languages


"""

error_ocr_no_reply = """reply to a photo to get the text"""

lang_saved_message = """**{} has been set as your main language.**"""

ocr_message_text = """```the text in the image:``` \n\n {}"""

translate_string_one = """**\ud83c\udf10 Translation**:\n\n```{}```\n\n**🔍 Detected language:** {} \n\n **Translated to**: {}"""

translate_string_two = (
    """**\ud83c\udf10 Translation**:\n\n```{}```\n\n**🔍 Detected language:** {}"""
)

inline_text_string_one = """Translate from {} to {}"""

error_msg_string = """**Error:**  \n\n ```{}``` \n\n"""

help_group_string = """To get help click on the button below"""


google_tr_api_err_msg = """**Error:**  \n\n ```this is not text or this is google translate api limit, please try again later.```"""

ocr_err_msg_lang = """the language code is not supported in the ocr try to found the language code by click on the link {}"""
