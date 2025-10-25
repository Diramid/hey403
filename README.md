<h1 align="center">
  🌐 Hey 403 - CLI Edition
  <br>
  <sub>⚡ DNS Accessibility Testing Tool ⚡</sub>
</h1>

<div align="center">

[![Stars](https://img.shields.io/github/stars/Diramid/hey-403-cli?logo=starship&color=gold)](https://github.com/Diramid/hey-403-cli/stargazers)
[![Forks](https://img.shields.io/github/forks/Diramid/hey-403-cli?logo=git&color=9cf)](https://github.com/Diramid/hey-403-cli/forks)
[![Issues](https://img.shields.io/github/issues/Diramid/hey-403-cli?logo=github&color=red)](https://github.com/Diramid/hey-403-cli/issues)
[![License](https://img.shields.io/github/license/Diramid/hey-403-cli?logo=open-source-initiative&color=green)](https://github.com/Diramid/hey-403-cli/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/hey403?logo=pypi&color=blue)](https://pypi.org/project/hey403/)
[![PyPI Downloads](https://static.pepy.tech/badge/hey403)](https://pepy.tech/projects/hey403)


</div>

---

## 📖 What is Hey 403?
**Hey 403 - CLI Edition** is your go-to command-line tool for diagnosing domain accessibility issues across multiple DNS providers. Built for developers, network admins, and security enthusiasts, it helps you uncover:

- 🚫 **Geo-restrictions & Censorship**: Spot blocks instantly.
- 🌍 **DNS Inconsistencies**: Compare resolutions globally.
- 🔄 **Server Variations**: Detect response differences.
- 🔍 **Connectivity Issues**: Pinpoint problems fast.

### Why Hey 403?
- ⚡ **Lightning-Fast**: Get results in seconds with parallel testing.
- 🌐 **Global Scope**: Test with 15+ DNS servers worldwide.
- 🔧 **Actionable Insights**: Troubleshoot DNS issues like a pro.
- 📊 **Pretty Output**: Colorful, rich terminal formatting.

---

## ✨ Features
| Feature             | Description                              |
|---------------------|------------------------------------------|
| 🚪 **CLI-First**    | Built for the terminal, no GUI nonsense. |
| 🌍 **15+ DNS**      | Preloaded with top global DNS providers. |
| ⚡ **Parallel Tests**| Concurrent checks for speed.            |
| 🎨 **Rich Output**  | Eye-catching, formatted results.         |
| 🔧 **DNS Control**  | Set or unset DNS directly from the CLI.  |
| 📊 **Export Data**  | Save results in CSV and JSON formats.    |

---

## 🚀 Get Started
1. **Install it**:
   ```bash
   pip install hey403
   ```
2. **Check the help**:
   ```bash
   hey403 --help
   ```
3. **Test a domain**:
   ```bash
   hey403 example.com
   ```

---

## 🔧 Usage Examples
```bash
# Test a domain across all DNS providers
hey403 example.com

# Set the fastest DNS for your system
hey403 example.com --set

# Check your current DNS
hey403 -c

# Revert to default DNS
hey403 --unset
```

See all options with `hey403 --help`!

---

## 🤝 Contributing
Love Hey 403? Help make it better!
1. Fork it 🍴
2. Set up your dev environment:
   ```bash
   git clone https://github.com/Diramid/hey-403-cli.git
   cd hey-403-cli
   pip install -e .[dev]
   ```
3. Test your changes:
   ```bash
   pytest tests/ -v
   ```
4. Push & PR:
   ```bash
   git checkout -b feature/cool-stuff
   git commit -m "Add cool stuff"
   git push origin feature/cool-stuff
   ```
5. Open a Pull Request on [GitHub](https://github.com/Diramid/hey-403-cli/pulls)

Check out our [Contributing Guide](CONTRIBUTING.md) for more!

---

## ⚖️ License
Hey 403 is proudly open-source under the [MIT License](LICENSE). Use it, tweak it, share it—just keep it legal!

---

## 🌟 Show Your Support
- ⭐ Star us on [GitHub](https://github.com/Diramid/hey-403-cli)!
- 🐛 Report bugs or suggest features in [Issues](https://github.com/Diramid/hey-403-cli/issues).
- 💬 Join the conversation—tell us how you use Hey 403!

---

> **Heads Up!** 📢  
> Use Hey 403 responsibly and respect local laws. Unauthorized system access is a no-go.
