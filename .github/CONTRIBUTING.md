# Contributing to SkillBot

Thank you for your interest in contributing to SkillBot! Here's how you can help.

## Code Style

- Use type hints for function parameters and return values
- Follow PEP 8 guidelines
- Write docstrings for classes and functions
- Keep functions focused and single-purpose

## Development Process

1. **Fork & Clone**
   ```bash
   git clone https://github.com/yourusername/skillbot.git
   cd skillbot
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

3. **Create Feature Branch**
   ```bash
   git checkout -b feature/YourFeature
   ```

4. **Make Changes & Test**
   - Write tests for new features
   - Ensure all tests pass
   - Update documentation

5. **Submit Pull Request**
   - Write clear PR description
   - Reference any related issues
   - Wait for review

## Testing

Run tests using:
```bash
python -m pytest tests/
```

## Documentation

- Update README.md for major changes
- Add docstrings to new functions
- Include example usage where appropriate

## Code Review Process

1. Automated checks must pass
2. At least one maintainer review
3. All comments addressed
4. Documentation updated