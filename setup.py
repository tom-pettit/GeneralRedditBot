from distutils.core import setup
setup(
  name = 'RedditBotClass',         
  packages = ['RedditBotClass'],   
  version = '1.1.0',     
  license='MIT',        
  description = 'A library used to create reddit bots, with some pre-written functions for the bots.',  
  author = 'Tom Pettit',                  
  author_email = 'tompettit36@gmail.com',     
  url = 'https://github.com/tom-pettit/RedditBotClass',   
  download_url = 'https://github.com/tom-pettit/RedditBotClass/archive/v1.1.0.tar.gz',   
  keywords = ['RedditBotClass', 'reddit bot', 'bot', 'reddit', 'praw', 'reddit-bot', 'bots'],   
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
