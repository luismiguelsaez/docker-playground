import http from 'k6/http';
import { URL } from 'https://jslib.k6.io/url/1.0.0/index.js';
import { randomItem } from 'https://jslib.k6.io/k6-utils/1.2.0/index.js';
import { textSummary } from 'https://jslib.k6.io/k6-summary/0.0.2/index.js';

export const options = {
  scenarios: {
    open_model: {
      executor: 'ramping-arrival-rate',
      startRate: 10,
      timeUnit: '1s',
      preAllocatedVUs: 2,
      maxVUs: 10,
      startTime: '0s',
      stages: [
        { target: 5, duration: '10s' },
        { target: 10, duration: '20s' },
        { target: 5, duration: '20s' },
      ],
    },
  },
};

const data = [
  {
    'text': 'Esto es una prueba de rendimiento',
    'language': 'es'
  },
  {
    'text': 'This is a performance test',
    'language': 'en'
  },
  {
    'text': 'Esto hes una prueva de rendimiento',
    'language': 'es'
  },
  {
    'text': 'Tis is ha performmance test',
    'language': 'en'
  },
  {
    'text': 'Dies ist ein Leistungstest',
    'language': 'de'
  },
  {
    'text': 'In the performance test, we increase the length of the string to see if it impacts performance noticeably',
    'language': 'en'
  },
  {
    'text': 'En la prueba de rendimiento, incrementamos la longitud de la cadena para ver si esto impazta al rendimiento de forma apreciable',
    'language': 'es'
  },
  {
    'text': 'Im Leistungstest erhöhen wir die Saitenlänge, um zu sehen, ob sich dies spürbar auf die Leistung auswirkt.',
    'language': 'de'
  },
  {
    'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dfsfsfsfsf eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'language': 'es'
  },
  {
    'text': 'This indicates that you can make low-cost international calls. Select regular calls for reliability or Internet calls for the lowest rates.',
    'language': 'en'
  },
  {
    // Text in Russian 
    'text': 'В этом случае вы можете совершать международные звонки по низким тарифам. Выберите обычные звонки для надежности или Интернет-звонки для самых низких тарифов.',
    'language': 'ru'
  } ,
  {
    // Text in Arabic
    'text': 'هذا يشير إلى أنه يمكنك إجراء مكالمات دولية بتكلفة منخفضة. حدد المكالمات العادية للموثوقية أو المكالمات عبر الإنترنت للحصول على أقل الأسعار.',
    'language': 'ar'
  }
];

export default function () {

  const url = new URL('http://localhost:8010/v2/check');

  const randomParams = randomItem(data);

  url.searchParams.append('text', randomParams['text']);
  url.searchParams.append('language', randomParams['language']);
  url.searchParams.append('disabledRules', 'FRENCH_WHITESPACE,BRAK_KROPKI,OT_EINDE_ZIN_ONVERWACHT,WORD_CONTAINS_UNDERSCORE,UPPERCASE_SENTENCE_START,EN_QUOTES');

  const params = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  };

  const res = http.post(url.toString(), params);

  console.log('Response[' + res.status + ']: ' + res.body);
}

export function handleSummary(data) {
  return {
    'stdout': textSummary(data, { indent: ' ', enableColors: true }),
    'summary.json': JSON.stringify(data),
  };
}
