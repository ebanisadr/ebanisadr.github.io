---
category: Recipe
title: Roasted Chickpeas
date: Janurary 16, 2026
time: 10 minutes prep, 30 minutes roast
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

## Pantry

- [ ] 16 oz can of chickpeas (I like STO low sodium)

### Seasoning options

* smoked paprika, garlic+onion powder, salt
* tajin (+lime zest)
* ask chatgpt

## Instructions

 - [ ] oven at 400-425
 - [ ] drain + dry chickpeas
 - [ ] toss with oil + seasonings (go hard here; more than most roasted veggies)
 - [ ] roast ~30 minutes tossing midway

<br />
<hr/>
<br />

It's really that easy. Still workshopping the seasoning options (first one was kinda bland) but I love this concept.

1 can = quarter sheet = half a 16 oz jar
