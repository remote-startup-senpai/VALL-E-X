infer_from_audio_examples = [
    [
        "This is how this machine has taken my voice.",
        "English",
        "no-accent",
        "prompts/en-2.wav",
        None,
        "Wow, look at that! That's no ordinary Teddy bear!",
    ],
    [
        "我喜欢抽电子烟，尤其是锐刻五代。",
        "中文",
        "no-accent",
        "prompts/zh-1.wav",
        None,
        "今天我很荣幸，",
    ],
    [
        "私の声を真似するのはそんなに面白いですか？",
        "日本語",
        "no-accent",
        "prompts/ja-female-1.wav",
        None,
        "名鑑レベルが上がったそうです。知らない間に",
    ],
    [
        "私の声を真似するのはそんなに面白いですか？",
        "日本語",
        "no-accent",
        "prompts/ja-female-2.wav",
        None,
        "初めまして、朝武よしのです。",
    ],
    [
        "どうでもいい",
        "日本語",
        "no-accent",
        "prompts/ja-male-1.wav",
        None,
        "無理だったかもしれない。無茶だったかもしれない。でも、無駄じゃなかった。",
    ],
    [
        "この会社は最高だぜ！",
        "日本語",
        "no-accent",
        "prompts/ja-male-2.wav",
        None,
        "羽川がなんでもしてくれるの？やった！",
    ],
    ["你可以听得出来我有多困。", "中文", "no-accent", "prompts/en-1.wav", None, ""],
    ["この文は、クロスリンガル合成の例です。", "日本語", "no-accent", "prompts/zh-2.wav", None, ""],
    [
        "Actually, I can't speak English, but this machine helped me do it.",
        "English",
        "no-accent",
        "prompts/ja-female-1.wav",
        None,
        "",
    ],
]

make_npz_prompt_examples = [
    [
        "Gem-trader",
        "prompts/en-2.wav",
        None,
        "Wow, look at that! That's no ordinary Teddy bear!",
    ],
    ["Ding Zhen", "prompts/zh-1.wav", None, "今天我很荣幸，"],
    ["Yoshino", "prompts/ja-female-2.wav", None, "初めまして、朝武よしのです。"],
    ["Sleepy-woman", "prompts/en-1.wav", None, ""],
    ["Yae", "prompts/zh-2.wav", None, ""],
    ["Cafe", "prompts/ja-female-1.wav", None, "名鑑レベルが上がったそうです。知らない間に"],
    [
        "Koyomi",
        "prompts/ja-male-1.wav",
        None,
        "無理だったかもしれない。無茶だったかもしれない。でも、無駄じゃなかった。",
    ],
]

infer_from_prompt_examples = [
    [
        (
            "A prompt contains voice, prosody and emotion information of a"
            " certain speaker."
        ),
        "English",
        "no-accent",
        "vctk_1",
        None,
    ],
    [
        "This prompt is made with an audio of three seconds.",
        "English",
        "no-accent",
        "librispeech_1",
        None,
    ],
    [
        "This prompt is made with Chinese speech",
        "English",
        "no-accent",
        "seel",
        None,
    ],
]
