# Changelog - Version 2.0 (September 2026)

## 🔄 নতুন ফিচার (New Features)

### ✨ Registration No এবং Roll No যোগ করা হয়েছে
- বিশ্ববিদ্যালয় নির্দিষ্ট registration number সংরক্ষণ
- Roll number স্বয়ংক্রিয়ভাবে জেনারেট করা
- myccAcc.txt এ সম্পূর্ণ তথ্য সংরক্ষণ

### 📍 Address Field যোগ করা হয়েছে
- Street Address
- City
- State
- ZIP Code
- সম্পূর্ণ ঠিকানা ডেটাবেস সংরক্ষণ

### 🎓 University Database
- বাংলাদেশের ১০টি বিশ্ববিদ্যালয় ডেমো
- ইউএসএর ১০টি বিশ্ববিদ্যালয় ডেমো
- Department-wise email format সমর্থন

## 🔧 আপডেট (Updates)

### helper.py
- User-Agent আপডেট করা হয়েছে (Chrome 120.0.0.0 এর জন্য)
- Error handling উন্নত করা হয়েছে
- Timeout configuration যোগ করা হয়েছে
- Real-time token generation

### bot.py
- Form field validation উন্নত করা হয়েছে
- Registration No এবং Roll No input fields যোগ করা হয়েছে
- Address parsing logic আপডেট করা হয়েছে
- Selenium selectors পুনরায় যাচাই করা হয়েছে

### setup.py
- Package versions আপডেট করা হয়েছে
- python-dotenv যোগ করা হয়েছে
- Improved error handling
- Browser selection উন্নত করা হয়েছে

## 🐛 বাগ ফিক্স (Bug Fixes)

- Fixed deprecated Selenium methods (find_element_by_* → find_element)
- Fixed Chrome driver initialization issues
- Improved Incapsula bypass reliability
- Better handling of network timeouts
- Fixed address validation errors

## 📊 Performance Improvements

- Faster token generation
- Optimized form filling speed
- Better memory management
- Reduced API call timeouts

## ⚙️ Technical Changes

### Dependencies Updated
```
selenium >= 4.10.0
undetected-chromedriver >= 3.5.0
selenium-wire >= 5.1.0
requests >= 2.31.0
colorama >= 0.4.6
```

### Python Version
- Minimum: Python 3.8
- Recommended: Python 3.9+

## 📝 Documentation

- DEMO_EMAILS.md যোগ করা হয়েছে
- বাংলা এবং ইংরেজি উভয় ভাষায় ডকুমেন্টেশন
- বিশ্ববিদ্যালয় ফরম্যাট গাইড

## ⚠️ Breaking Changes

None - সম্পূর্ণ পিছিয়ে সামঞ্জস্যপূর্ণ (Fully backward compatible)

## 📌 Known Issues

- কিছু প্রক্সি সেবা Incapsula বাইপাস ব্লক করতে পারে
- reCAPTCHA সমাধান দীর্ঘ সময় নিতে পারে
- নির্দিষ্ট সময়ে OpenCCC সার্ভার স্লো হতে পারে

## 🔜 আসন্ন ফিচার (Coming Soon)

- Multi-account generation
- Database integration
- Web UI dashboard
- Email verification automation
- Batch processing

---

**Release Date:** September 11, 2026
**Maintained By:** Si-Edu-Mail-Generator Team
