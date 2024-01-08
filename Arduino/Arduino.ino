#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// Inisialisasi objek LCD
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Alamat I2C LCD umumnya adalah 0x27, sesuaikan jika alamat berbeda

void setup() {
  Serial.begin(9600);  // Memulai koneksi serial
  lcd.init();          // Inisialisasi LCD
  lcd.backlight();     // Nyalakan backlight LCD
  lcd.clear();         // Bersihkan layar LCD
}

void loop() {
  if (Serial.available() > 0) {
    // Jika data tersedia di serial
    String data = Serial.readStringUntil('\n'); // Baca data dari serial sampai karakter newline (\n)
    
    // Tampilkan data pada LCD
    lcd.setCursor(0, 0);  // Set kursor ke kolom 0, baris 0
    lcd.print("Slot Tersedia : ");
    lcd.setCursor(15, 0);  // Set kursor ke kolom 0, baris 1
    lcd.print(data);       // Tampilkan data yang diterima dari Python
  }
}
