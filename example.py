# example.py
# Bu örnek, db-ally kütüphanesini kullanarak basit bir veritabanı sorgusu yapar

from dbally import DBAlly  # Gerekli sınıf veya fonksiyonu içe aktarın

# Veritabanı bağlantısını yapılandırma
db_ally = DBAlly(connection_string="sqlite:///your_database.db")

# Doğal dil ile sorgulama yapma
query = "List all employees in the sales department"
result = db_ally.query(query)

# Sonucu yazdırma
print(result)