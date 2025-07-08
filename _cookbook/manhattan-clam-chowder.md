---
title: Manhattan Clam Chowder
date: July 07, 2025
time: 30 minutes prep, 3-6 hour simmer
script: |-
  // todo: template rather than page specific
  (function(){
    const pageKey = window.location.pathname;
    const ONE_WEEK_MS = 7 * 24 * 60 * 60 * 1000;
  
    document.querySelectorAll('li > input[type="checkbox"]').forEach(cb => {
      // 1) Make it clickable if still disabled
      if (cb.hasAttribute('disabled')) {
        cb.removeAttribute('disabled');
      }
  
      // derive a unique key for this checkbox
      const labelText = (cb.nextSibling.textContent || '').trim();
      const storageKey = `${pageKey}::${labelText}`;
  
      // 2) Try to load saved state
      try {
        const stored = JSON.parse(localStorage.getItem(storageKey));
        if (stored && stored.expires > Date.now()) {
          cb.checked = stored.checked;
        } else {
          // 3) expired or invalid → clean up
          localStorage.removeItem(storageKey);
        }
      } catch(_) {
        localStorage.removeItem(storageKey);
      }
  
      // 4) On change, save new state + fresh expiration
      cb.addEventListener('change', () => {
        const record = {
          checked: cb.checked,
          expires: Date.now() + ONE_WEEK_MS
        };
        localStorage.setItem(storageKey, JSON.stringify(record));
      });
    });
  })();
---

### Groceries

bakery
 - [ ] crusty bread 🥖 😋 (i liked wfm ancient grains one)

groceries
- [ ] 1 med onion
- [ ] 3-4 sm carrots
- [ ] 2 celery stalks (leaves garnish)
- [ ] garlic
- [ ] 4 smallish waxy potatoes
- [ ] 1 lemon (optional, garnish)
 
 pantry
- [ ] 3-4 cans chopped clams IN CLAM JUICE (6.5 oz, snow's are good)
- [ ] 1 can diced tomatoes (14.5 oz)
- [ ] 2 T tomato paste
- [ ] red pepper flakes
- [ ] oregano
- [ ] bay leaf 🤷‍♀️
- [ ] EVOO, salt, pepper
- [ ] clam juice or seafood stock (can sub water)

### Instructions -- crockpot

Dice these
 - [ ] 1 med onion
 - [ ] 3-4 sm carrots
 - [ ] 2 stalks celery (leaves garnish)
 - [ ] 4 smallish waxy potatoes
 - [ ] 2 cloves garlic, minced

 Drop everything into the crockpot and open some cans
 - [ ] 1 can diced tomatoes (and juice)
 - [ ] 4 cans clam juice **(reserve clams!)**
 - [ ] 2 tablespoons tomato paste

Season
 - [ ] 2 T EVOO
 - [ ] ~1 T dried oregano
 - [ ] ~1 t red pepper flakes
 - [ ] bay leaf
 - [ ] salt and pepper

Fill with whatever you've got until everything's just shy of covered.

⬆️ prep until here ⬆️

Cook on low ~ 6h

Toast bread

Add clams just before serving, (pull bay leaf), garnish with celery leaves, lemon wedge

<hr/>

Makes about half a crockpot (can be doubled). Easy, tasty, decent food. Very high bang for buck.

I imagine this can be done better on the stove with sauteed aromatics and better-timed additions of veggies but I haven't tried it.

Ends up slightly mushy when I leave it cooking while I'm at the office; I'll try starting from cold and update eventually.
