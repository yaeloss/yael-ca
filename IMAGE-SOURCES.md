# Replacement image sources

Sources and rights statements checked on 15 September 2026. These replacements use public-domain or CC0 material. Credits are retained here for provenance. Hugo generates responsive WebP derivatives for the article pages; the six downloaded source images are otherwise unchanged.

## Federalist

- File: `content/posts/lessons-in-federalism/images/federalist.jpg`
- Work: Title page of The Federalist, volume I (1788).
- [Source and rights statement](https://commons.wikimedia.org/wiki/File:Federalist-1788.jpg)
- [Downloaded image](https://upload.wikimedia.org/wikipedia/commons/4/4c/Federalist-1788.jpg)
- Rights: Public domain; historical work with expired copyright.
- Notes: Original JPEG.

## Rubio

- File: `content/posts/rubio-wraps-up-week-long-audition-in-national/images/RubioRomney-570x3201.jpg1.jpg`
- Work: U.S. Senate official portrait of Marco Rubio, 28 January 2011.
- [Source and rights statement](https://commons.wikimedia.org/wiki/File:Marco_Rubio,_Official_Portrait,_112th_Congress_(cropped).jpg)
- [Downloaded image](https://upload.wikimedia.org/wikipedia/commons/8/80/Marco_Rubio%2C_Official_Portrait%2C_112th_Congress_%28cropped%29.jpg)
- Rights: Public domain in the United States; U.S. federal government work.
- Notes: Original JPEG of the crop supplied by Commons.

## Obama

- File: `content/posts/the-younger-generations-expectations-of-politics/images/Fact-check-Obamas-State-of-the-Union-2012-4GSS1QU-x-large.jpg`
- Work: Pete Souza / White House, Barack Obama delivering the State of the Union, 24 January 2012.
- [Source and rights statement](https://commons.wikimedia.org/wiki/File:2012_State_of_Union.jpg)
- [Downloaded image](https://upload.wikimedia.org/wikipedia/commons/f/f5/2012_State_of_Union.jpg)
- Rights: Public domain in the United States; U.S. federal government work.
- Notes: Original JPEG.

## Washington

- File: `content/posts/george-washingtons-farewell-address/images/George_Washington.jpg`
- Work: Gilbert Stuart, Lansdowne portrait of George Washington (1796), National Portrait Gallery, Smithsonian Institution.
- [Source and rights statement](https://commons.wikimedia.org/wiki/File:Gilbert_Stuart,_George_Washington_(Lansdowne_portrait,_1796).jpg)
- [Downloaded image](https://upload.wikimedia.org/wikipedia/commons/1/12/Gilbert_Stuart%2C_George_Washington_%28Lansdowne_portrait%2C_1796%29.jpg)
- Rights: Public domain; faithful reproduction of an artwork with expired copyright. Smithsonian also labels the object CC0: https://www.si.edu/object/npg_NPG.2001.13
- Notes: Original JPEG.

## Vienna

- File: `content/posts/honor-system-on-viennese-public-transit/images/ubahn-nc.jpg`
- Work: Tokfo, platforms at U3 Gasometer station, Vienna, 18 September 2014.
- [Source and rights statement](https://commons.wikimedia.org/wiki/File:U3_Gasometer.jpg)
- [Downloaded image](https://thumb.wikimedia.org/wikipedia/commons/thumb/0/07/U3_Gasometer.jpg/1280px-U3_Gasometer.jpg)
- Rights: CC0 1.0 Universal public-domain dedication.
- Notes: 1280-pixel Commons thumbnail; caption identifies this as a 2014 illustration of the older article.

## Deworm

- File: `content/posts/a-new-way-to-do-good-promises-to-provide-the-data-to-make-the-biggest-impact-effective-altruism/images/deworming-dien-bien-2012.jpg`
- Work: Richard Nyberg / USAID Vietnam, schoolchildren receiving deworming medicine in Dien Bien (31 October 2012).
- [Source and rights statement](https://commons.wikimedia.org/wiki/File:School_children_receive_a_dose_of_deworming_medicine_in_Dien_Bien_(8141220279).jpg)
- [Downloaded image](https://thumb.wikimedia.org/wikipedia/commons/thumb/8/83/School_children_receive_a_dose_of_deworming_medicine_in_Dien_Bien_%288141220279%29.jpg/1280px-School_children_receive_a_dose_of_deworming_medicine_in_Dien_Bien_%288141220279%29.jpg)
- Rights: Public domain in the United States; U.S. federal government work.
- Notes: 1280-pixel Commons thumbnail. Replaces the invalid Deworm-1-1024x699.png; caption identifies the actual location and photographer, without assigning it to a charity mentioned in the article.

## Historical pay chart

- File: `content/posts/public-versus-private-pay/images/fedpay.jpg`
- Newly drawn bar chart using the twelve wage figures already quoted in the article; no third-party chart artwork was copied.
- Figures are explicitly labeled 2009, with the article’s attribution to the Bureau of Labor Statistics. The underlying BLS dataset has not been independently revalidated.
- The numbers remain available as article text for accessibility and search.
- Reproduce using Pillow and a sans-serif TTF font: `python3 scripts/generate_pay_chart.py --font /path/to/font.ttf`. This optional script is not required by Hugo or CI.

## Unrecoverable graphics

The Effective Altruism article no longer embeds `images/grafik1.jpg` or `images/grafik2-1024x537.jpg`. Both contain invalid image data, and their original contents could not be established. The files remain in the source bundle for recovery; no replacement data or diagrams were invented.

## Missing legacy files

During verification, five additional embeds in the repaired articles pointed to files absent from the repository. Their broken embeds were removed; article text was retained. The original graphics could not be reliably identified from their filenames.

- `content/posts/lessons-in-federalism/images/400px-The_new_European_Federation.png`
- `content/posts/lessons-in-federalism/images/US_Federal_Outlay_and_GDP_linear_graph_t670.png`
- `content/posts/lessons-in-federalism/images/cama.gif`
- `content/posts/the-younger-generations-expectations-of-politics/images/130278.jpg`
- `content/posts/the-younger-generations-expectations-of-politics/images/teapartywallstreet.jpg`

## Rights verification scope

The six replacement source images have explicit public-domain or CC0 statements on the linked file pages; the pay chart was drawn anew. No replacement relies on a paid stock license, CC BY, CC BY-SA, or a noncommercial-only license. This review covers the seven replacements, not the website’s pre-existing images.

The Rubio, Obama, and USAID photographs are specifically identified as U.S. federal government works in the public domain in the United States. This is not a certification of their status in every jurisdiction. Public-domain/CC0 status also does not clear every possible privacy, publicity, or trademark right; see the [CC0 deed](https://creativecommons.org/publicdomain/zero/1.0/).

### SHA-256 of installed replacement files

These hashes identify the exact files reviewed, before Hugo generates WebP derivatives.

- `content/posts/lessons-in-federalism/images/federalist.jpg`: `4466aee50476b57fcbd13a91eab171fe1b43c04b908eb7fa1c1122cbac4e0406`
- `content/posts/rubio-wraps-up-week-long-audition-in-national/images/RubioRomney-570x3201.jpg1.jpg`: `59a51d5159402705f26e2dff7dd69f82829e96a06efe6659e7cf1457cc113531`
- `content/posts/the-younger-generations-expectations-of-politics/images/Fact-check-Obamas-State-of-the-Union-2012-4GSS1QU-x-large.jpg`: `53bb08a55fa3723682120ead692bf67796440a32ee270cd654b4487068cb9bdd`
- `content/posts/george-washingtons-farewell-address/images/George_Washington.jpg`: `007e8edfd3d13b67001782a27601b10336e0adfab551506345754d5b564e6666`
- `content/posts/honor-system-on-viennese-public-transit/images/ubahn-nc.jpg`: `1911ecbb6970871dbb98ca05c587689f19dc49c4b782da68f8a29bd4b74d77d8`
- `content/posts/a-new-way-to-do-good-promises-to-provide-the-data-to-make-the-biggest-impact-effective-altruism/images/deworming-dien-bien-2012.jpg`: `42654f01776660c578fe7dd8b58d77b915aa6cdcaf5b042a8f7ac36c4cd29ee0`
- `content/posts/public-versus-private-pay/images/fedpay.jpg`: `634eaab2d79f7f72b591e05bbe740e817a637257ab9d7fa87d5c8f67ddd2d491`
