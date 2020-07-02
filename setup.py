from distutils.core import setup
setup(
  name = 'GeneralRedditBot',         
  packages = ['GeneralRedditBot'],   
  version = '2.0.0',     
  license='MIT',        
  description = 'A library used to create general subreddit bots using some pre-written functions for the bots.',  
  author = 'Tom Pettit',                  
  author_email = 'tompettit36@gmail.com',     
  url = 'https://github.com/tom-pettit/GeneralRedditBot',   
  download_url = 'https://github.com/tom-pettit/GeneralRedditBot/archive/v2.0.0.tar.gz',   
  keywords = ['GeneralRedditBot', 'general reddit bot', 'reddit bot', 'bot', 'reddit', 'praw', 'reddit-bot', 'bots'],   
  install_requires=[            
          'praw',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.7',      
    'Programming Language :: Python :: 3.8',
  ],
)
