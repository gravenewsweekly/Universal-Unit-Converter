require 'sinatra'
require 'json'

conversion_factors = {
  "length" => { "meter" => 1, "kilometer" => 0.001, "mile" => 0.000621371, "foot" => 3.28084 },
  "weight" => { "kilogram" => 1, "gram" => 1000, "pound" => 2.20462, "ounce" => 35.274 },
}

def convert_temperature(value, from_unit, to_unit)
  case [from_unit, to_unit]
  when ["celsius", "fahrenheit"]
    (value * 9/5) + 32
  when ["fahrenheit", "celsius"]
    (value - 32) * 5/9
  else
    value
  end
end

get '/convert' do
  category = params[:category]
  value = params[:value].to_f
  from_unit = params[:from]
  to_unit = params[:to]

  result = if category == "temperature"
             convert_temperature(value, from_unit, to_unit)
           else
             factor = conversion_factors[category][to_unit] / conversion_factors[category][from_unit]
             value * factor
           end

  { result: result }.to_json
end
