# Hey 403 - CLI Edition
**⚡ A Command-Line DNS Accessibility Testing Tool ⚡**

Hey 403 is a powerful Python-based CLI utility designed to diagnose domain accessibility issues across multiple DNS providers. Whether you're a developer, network administrator, or security enthusiast, Hey 403 helps you quickly identify geo-restrictions, DNS inconsistencies, and connectivity problems.

---

## Key Features
- **Global DNS Testing**: Test domain accessibility with **15+ preconfigured DNS servers** from providers like Google, Cloudflare, and more.
- **Error Detection**: Detect **403 Forbidden**, censorship blocks, and other HTTP errors.
- **Performance Insights**: Measure and compare DNS resolution times across providers.
- **DNS Management**: Set or unset DNS configurations directly from the CLI.
- **Parallel Execution**: Run concurrent tests for faster results.
- **Rich Output**: Enjoy colorful, formatted output with the `rich` library.

---

## Installation
Install Hey 403 easily via PyPI:

```bash
pip install hey403
```

### Requirements
- Python 3.8+
- Dependencies: `rich`, `requests`, `dnspython` (automatically installed via pip)

---

## Quick Start
After installation, check the available options:

```bash
hey403 --help
```

Test a domain right away:

```bash
hey403 example.com
```

---

## Usage Examples
Here’s how you can use Hey 403:

### Test Domain Accessibility
Check how a domain resolves across multiple DNS providers:
```bash
hey403 example.com
```

### Set the Best DNS
Automatically set the fastest working DNS for your system:
```bash
hey403 example.com --set
```

### View Current DNS
Display your system’s current DNS settings:
```bash
hey403 -c
```

### Unset Custom DNS
Revert to your system’s default DNS:
```bash
hey403 --unset
```

---

## Command-Line Options
| Option            | Description                                   |
|-------------------|-----------------------------------------------|
| `-h, --help`      | Show help message and exit                   |
| `-c, --current-dns` | Display current DNS settings               |
| `--set`           | Set the fastest DNS from successful tests    |
| `--unset`         | Remove custom DNS and revert to default      |
| `--url URL`       | Specify an alternate URL to test             |

Run `hey403 --help` for full details.

---

## Why Hey 403?
- **Instant Diagnostics**: Identify DNS issues in seconds.
- **Global Reach**: Test with DNS servers worldwide.
- **User-Friendly**: Clean, colorful CLI output.
- **Customizable**: Manage DNS settings on the fly.

---

## Contributing
We welcome contributions! To get started:
1. Install the package in editable mode with dev dependencies:
   ```bash
   pip install -e .[dev]
   ```
2. Run tests:
   ```bash
   pytest tests/ -v
   ```
3. Submit your changes via a pull request on [GitHub](https://github.com/Diramid/hey-403-cli).

See our [Contributing Guide](https://github.com/Diramid/hey-403-cli/blob/main/CONTRIBUTING.md) for more details.

---

## License
Hey 403 is licensed under the [MIT License](https://github.com/Diramid/hey-403-cli/blob/main/LICENSE). Feel free to use, modify, and distribute it responsibly.

---

## Notes
- **Responsible Use**: Always comply with local laws and regulations when testing domains.
- **Feedback**: Have suggestions? Open an issue on [GitHub](https://github.com/Diramid/hey-403-cli/issues)!

---
