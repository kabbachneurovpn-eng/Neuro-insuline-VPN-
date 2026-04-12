from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

# بيانات المخترع والنظام
SYSTEM_CORE = {
    "founder": "Mohamed Kabbach",
    "project": "Neuro-Insulin VPN",
    "location": "Casablanca, Morocco",
    "contact": "+212600505075",
    "gumroad_link": "https://gumroad.com/l/your-dose-link" # ضع رابط متجرك هنا
}

# قاعدة بيانات وهمية للسيرفرات (للمحاكاة حالياً)
SERVERS = ["CASA-01", "RABAT-CORE", "MARRAKECH-GATE", "GLOBAL-INJECTION-07"]

@app.route('/')
def index():
    # هذا المسار سيخدم صفحة index.html التي صممناها
    return render_template('index.html')

@app.route('/v-search', methods=['POST'])
def v_search():
    data = request.json
    query = data.get('query', '').upper()
    
    # محاكاة البحث التقني
    time.sleep(1.5) # لإعطاء هيبة تقنية (Processing time)
    
    if any(srv in query for srv in SERVERS) or "ACTIVE" in query:
        status = "STABLE CONNECTION FOUND"
        code = f"NI-{random.randint(1000, 9999)}-SEC"
    else:
        status = "NODE NOT FOUND - SCANNING GLOBAL NETWORKS"
        code = "ERR-404-X"
        
    return jsonify({
        "status": status,
        "encryption_key": code,
        "founder_sig": SYSTEM_CORE["founder"]
    })

@app.route('/buy-dose', methods=['POST'])
def buy_dose():
    # هنا يتم توجيه المستخدم لعملية الربح
    return jsonify({
        "message": "Redirecting to Secure Payment Portal...",
        "redirect_url": SYSTEM_CORE["gumroad_link"]
    })

if __name__ == '__main__':
    print(f"--- [SYSTEM READY] ---")
    print(f"Welcome, {SYSTEM_CORE['founder']}")
    print(f"NI-INTELLIGENT CORE is starting on http://localhost:8080")
    app.run(host='0.0.0.0', port=8080, debug=True)

