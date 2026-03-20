# app.py - Website Multi-Halaman Pertamaku
import streamlit as st
import pandas as pd
import datetime
import pytz
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="Website Kerenku",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar untuk navigasi
st.sidebar.image("https://www.python.org/static/community_logos/python-logo-generic.svg", width=200)
st.sidebar.title("🌟 Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    ["🏠 Beranda", "📝 Tentang Saya", "🛠️ Project", "📞 Kontak"]
)

st.sidebar.markdown("---")
st.sidebar.info("Dibuat dengan ❤️ menggunakan Python & Streamlit")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📱 Scan Website")
st.sidebar.image("WebbQR.png", caption="Buka di HP", width=150)

# Set zona WIB
wib = pytz.timezone('Asia/Jakarta')
waktu_wib = datetime.datetime.now(wib)

# ========== HALAMAN BERANDA ==========
if menu == "🏠 Beranda":
    # Header dengan animasi
    st.markdown("""
        <style>
        .big-font {
            font-size: 50px !important;
            font-weight: bold;
            background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            padding: 30px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font">🚀 WELCOME TO MY WEBSITE</p>', unsafe_allow_html=True)
    
    # Kolom-kolom
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("📅 Hari Ini")
        hari = waktu_wib.strftime("%A, %d %B %Y")
        st.info(hari)
        if st.button("🎈 Klik Hadiah"):
            st.balloons()
    
    with col2:
        st.header("⏰ Jam WIB")
        jam = waktu_wib.strftime("%H:%M:%S")
        st.warning(jam)
        if st.button("❄️ Klik buat salju"):
            st.snow()
    
    with col3:
        st.markdown("### 👋 Siapa kamu?")
        nama = st.text_input("Masukkan nama:")
        if nama:
            st.success(f"Halo {nama}, selamat datang!")
    
    # Tampilkan gambar keren
    st.markdown("---")
    st.image("https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200", 
             caption="Coding itu asyik!")

# ========== HALAMAN TENTANG SAYA ==========
elif menu == "📝 Tentang Saya":
    st.title("📝 Tentang Saya")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", 
                width=250)
    
    with col2:
        st.markdown("""
        ### Halo, saya sedang belajar Python!
        
        **Perjalanan belajar saya:**
        - ✅ Install Python
        - ✅ Belajar dasar-dasar
        - ✅ Bikin program konversi PDF
        - ✅ Bikin website pertama
        - 🚗 Sekarang: belajar bikin website multi-halaman
        
        **Cita-cita:** Jadi programmer handal dan bikin startup sendiri!
        """)
    
    # Progress bar
    st.subheader("📊 Progress Belajar")
    progress = 0.65
    st.progress(progress)
    st.write(f"Udah {progress*100:.0f}%... semangat terus! 💪")
    
    # Skill
    st.subheader("🔧 Skill yang Udah Dipelajari")
    skills = {
        "Python Dasar": 80,
        "PDF Processing": 90,
        "Website dengan Streamlit": 75,
        "Problem Solving": 70
    }
    
    for skill, nilai in skills.items():
        st.write(f"{skill}:")
        st.progress(nilai/100)

# ========== HALAMAN PROJECT ==========
elif menu == "🛠️ Project":
    st.title("🛠️ Project-Project Saya")
    
    # Tabs untuk project
    tab1, tab2, tab3 = st.tabs(["📄 PDF to Text", "📝 PDF to Word", "🌐 Website"])
    
    with tab1:
        st.header("📄 Konversi PDF ke Teks")
        st.write("""
        **Fitur:**
        - Baca file PDF
        - Ekstrak teks dari setiap halaman
        - Simpan sebagai file .txt
        
        **Library:** PyPDF2
        """)
        
        uploaded_file = st.file_uploader("Coba upload PDF:", type=['pdf'])
        if uploaded_file:
            st.info("Fitur demo: file berhasil diupload!")
            st.balloons()
    
    with tab2:
        st.header("📝 Konversi PDF ke Word")
        st.write("""
        **Fitur:**
        - Konversi PDF ke format Word
        - Menjaga format dasar
        - Mudah diedit
        
        **Library:** popdf
        """)
        
    with tab3:
        st.header("🌐 Website dengan Streamlit")
        st.write("""
        **Fitur:**
        - Multi-halaman
        - Sidebar navigasi
        - Efek interaktif (balon, salju)
        - Responsive design
        
        **Library:** streamlit
        """)
        
        if st.button("Lihat demo efek"):
            st.balloons()
            st.snow()

# ========== HALAMAN KONTAK ==========
elif menu == "📞 Kontak":
    st.title("📞 Hubungi Saya")
    
    # Buat 2 kolom
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📧 Email")
        st.info("📩 **adimulyadi1980@gmail.com**")
        
        # Tombol copy email (simulasi)
        if st.button("📋 Copy Email"):
            st.success("Email berhasil di-copy!")
            st.balloons()
    
    with col2:
        st.markdown("### 📱 WhatsApp")
        st.success("📞 **+62 813 390 522 31**")
        
        # Tombol chat WhatsApp (bisa langsung klik)
        wa_link = "https://wa.me/6281339052231"
        st.markdown(f"[💬 Klik untuk Chat WhatsApp]({wa_link})")
    
    # Form pesan (opsional)
    st.markdown("---")
    st.markdown("### ✉️ Kirim Pesan Langsung")
    
    with st.form("contact_form"):
        nama = st.text_input("Nama Lengkap")
        email = st.text_input("Email Kamu")
        pesan = st.text_area("Pesan")
        
        submitted = st.form_submit_button("📨 Kirim Pesan")
        if submitted:
            if nama and email and pesan:
                st.success("✅ Pesan demo terkirim! (Ini hanya simulasi)")
                st.balloons()
            else:
                st.error("❌ Mohon isi semua field!")
    
    # Info tambahan
    st.markdown("---")
    st.caption("📌 Respons cepat dalam 1x24 jam")
Tambah QR code dan fix footer
# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 20px;'>
    © 2024 - Website Kerenku | Dibuat dengan Python dan Streamlit 🚀<br>
    <small>Terima kasih DeepSeek sudah membantu belajar!</small>
    </div>
    """, 
    unsafe_allow_html=True
)
