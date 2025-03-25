import sqlite3
import os
import random

class QuoteModel:
    def __init__(self):
        self.db_name = 'quotes.db'
        self.init_db()
    
    def init_db(self):
        # Delete the existing database if it exists
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
            
        # Create new database with Arabic quotes
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                author TEXT NOT NULL
            )
        ''')
        
        # Add some sample quotes in Arabic
        quotes = [
            ("العلم في الصغر كالنقش على الحجر", "حسن البصري"),
            ("الكتاب خير جليس في الزمان", "الجاحظ"),
            ("قيمة كل امرئ ما يحسنه", "الإمام علي"),
            ("من جد وجد ومن زرع حصد", "مثل عربي"),
            ("الصبر مفتاح الفرج", "مثل عربي"),
            ("الوقت كالسيف إن لم تقطعه قطعك", "مثل عربي"),
            ("إذا تم العقل نقص الكلام", "مثل عربي"),
            ("كن عالماً، فإن لم تستطع فكن متعلماً، فإن لم تستطع فأحب العلماء، فإن لم تستطع فلا تبغضهم", "الإمام الشافعي"),
            ("من سار على الدرب وصل", "مثل عربي"),
            ("الأدب جمال الفقير وستر الغني", "مثل عربي"),
            # Additional quotes
            ("العلم نور", "مثل عربي"),
            ("اطلبوا العلم من المهد إلى اللحد", "حديث نبوي"),
            ("خير الكلام ما قل ودل", "مثل عربي"),
            ("الحكمة ضالة المؤمن", "حديث نبوي"),
            ("لسانك حصانك إن صنته صانك وإن خنته خانك", "مثل عربي"),
            ("رب صدفة خير من ألف ميعاد", "مثل عربي"),
            ("الكلام كالدواء، إن أقللت منه نفع وإن أكثرت منه قتل", "مثل عربي"),
            ("إذا عرف السبب بطل العجب", "مثل عربي"),
            ("العمر هبة، والعلم كنز، والعمل مجد", "مثل عربي"),
            ("لا تؤجل عمل اليوم إلى الغد", "مثل عربي"),
            ("من علّمني حرفاً كنت له عبداً", "الإمام علي"),
            ("سلامة الإنسان في حفظ اللسان", "مثل عربي"),
            ("إنما الأمم الأخلاق ما بقيت", "أحمد شوقي"),
            ("تجري الرياح بما لا تشتهي السفن", "المتنبي"),
            ("يد واحدة لا تصفق", "مثل عربي"),
            ("العتاب هدية الأحباب", "مثل عربي")
        ]
        
        c.executemany('INSERT INTO quotes (text, author) VALUES (?, ?)', quotes)
        conn.commit()
        conn.close()
    
    def get_random_quote(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('SELECT * FROM quotes')
        quotes = c.fetchall()
        conn.close()
        
        # Select a random quote
        return random.choice(quotes)
